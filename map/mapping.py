from django.contrib.gis.gdal import DataSource
from pyunpack import Archive
from tempfile import NamedTemporaryFile
import os, re, requests


class UploadToDataSource(object):

    def __init__(self, request, file_param, url_param, *args, **kwargs):
        super(UploadToDataSource, self).__init__(*args, **kwargs)
        self.request = request
        self.file_param = file_param
        self.url_param = url_param
        if self.request.user.is_superuser and self.request.FILES and self.file_param in self.request.FILES:
            self.zip_file_path = self.request.FILES[file_param].temporary_file_path()
        elif self.url_param in self.request.POST:
            download_req = requests.get(self.request.POST[self.url_param], stream=True, headers={'User-Agent': 'bernadvisorybot http://bernadvisory.org'})
            with NamedTemporaryFile(delete=False) as f:
                for chunk in download_req.iter_content(chunk_size=1024): 
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
            self.zip_file_path = f.name

    def unzip_file(self):
        self.zip_ref = Archive(self.zip_file_path)
        self.shapefile_dir = os.path.join(os.path.dirname(self.zip_file_path), os.path.basename(self.zip_file_path).split('.')[0] + "-unzipped")
        self.zip_ref.extractall(self.shapefile_dir, auto_create_dir=True)
        return True

    def find_shapefile(self):
        backup_file = None
        # could fail if there's an infinitely recursive directory out there?
        # :dice_roll_emoji:
        for root, dirs, files in os.walk(self.shapefile_dir):
            for _file in files:
                if _file.endswith(".shp"):
                    self.shapefile_file = os.path.join(root, _file)
                    # this little construct gives preferential treatment
                    # to .shp files with keywords
                    # if re.search(r'precinct|votdst|politic', _file, flags=re.I):
                    return True
        # and this is our backup
        if self.shapefile_file:
            return True
        return False

    def get_shapefile_data(self):
        self.data_source = DataSource(self.shapefile_file)[0]
        return self.data_source

    def process(self):
        if self.request.FILES['shapefile'].name.endswith('.zip'):
            self.unzip_file()
            if self.find_shapefile():
                return self.get_shapefile_data()
        # elif self.request.FILES['shapefile'].name.endswith('.shp'):
        #     self.shapefile_file = self.zip_file_path
        #     self.data_source = DataSource(self.shapefile_file)[0]
        #     return self.data_source
        return "Sorry bro"