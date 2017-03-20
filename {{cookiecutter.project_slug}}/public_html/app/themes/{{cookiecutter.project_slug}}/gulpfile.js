var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var reload      = browserSync.reload;
var sass        = require('gulp-sass');
var concat      = require('gulp-concat');
var uglify      = require('gulp-uglify');

var src = {
  scss: 'assets/scss/**/*.scss',
  css:  'assets/stylesheets/',
  php:  '**/*.php',
  js:   'assets/javascripts/**/*.js'
};

/**
 * Watching files for changes
 */
gulp.task('watch', ['sass'], function() {
  browserSync.init({
    proxy: 'assainimmob.lo'
  });

  gulp.watch(src.scss, ['sass']);
  gulp.watch(src.js, ['scripts']);
  gulp.watch(src.php).on('change', reload);
});

/**
 * Compile Sass
 */
gulp.task('sass', function() {
  return gulp.src(src.scss)
    .pipe(sass({
      outputStyle: 'compressed'
    }).on('error', sass.logError))
    .pipe(gulp.dest(src.css))
    .pipe(reload({stream: true}));
});

/**
 * Concat & uglify JavaScript
 */
gulp.task('scripts', function() {
  gulp.src(src.js)
    .pipe(concat('production.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('javascripts'))
    .pipe(reload({stream: true}));
});

gulp.task('default', ['watch']);