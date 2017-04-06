var gulp = require('gulp'),
  sass = require('gulp-sass'),
  watch = require('gulp-watch'),
  minifycss = require('gulp-minify-css'),
  rename = require('gulp-rename'),
  gzip = require('gulp-gzip'),
  livereload = require('gulp-livereload'),
  autoprefixer = require('gulp-autoprefixer'),
  sourcemaps = require('gulp-sourcemaps'),
  gulpcopy = require('gulp-copy'),
  imagemin = require('gulp-imagemin'),
  changed = require('gulp-changed');

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

/* Compile SASS */
gulp.task('sass', function() {
    return gulp.src('map/static/scss/main.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(autoprefixer({
            browsers: ['last 2 versions','iOS 7', 'iOS 8', 'ie 9-11', 'android >= 4.2'],
            cascade: false
        }))
        .pipe(gulp.dest('map/static/dist/css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('map/static/dist/css'))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest('map/static/dist/css'))
        .pipe(livereload());
});

/* Optimize Images */
gulp.task('images', function() {
  return gulp.src('map/static/img/**')
    .pipe(changed('map/static/dist/img/'))
    .pipe(imagemin())
    .pipe(gulp.dest('map/static/dist/img/'))
});

/* Copy Fonts to Dist */
gulp.task('fonts', function() {
  return gulp.src('map/static/fonts/**/*')
    .pipe(gulp.dest('map/static/dist/fonts'))
})

/* Watch Files For Changes */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('map/static/scss/**/*.scss', ['sass'], {interval: 500}, ['sass']);

    /* Trigger a live reload on any Django template changes */
    gulp.watch('**/templates/*').on('change', livereload.changed);

});

gulp.task('default', ['sass', 'watch', 'images', 'fonts']);

gulp.task('build', ['sass', 'images', 'fonts']);
