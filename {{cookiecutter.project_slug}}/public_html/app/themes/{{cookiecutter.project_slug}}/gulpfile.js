var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var reload      = browserSync.reload;
var sass        = require('gulp-sass');
var concat      = require('gulp-concat');
var uglify      = require('gulp-uglify');
var rename      = require('gulp-rename');
var svgSymbols  = require('gulp-svg-symbols');
var runSequence = require('run-sequence');
var prefix      = require('gulp-autoprefixer');

var src = {
  scss: 'assets/scss/**/*.scss',
  css:  'assets/stylesheets/',
  icons: 'assets/icons/*.svg',
  php:  '**/*.php',
  js:   'assets/javascripts/**/*.js'
};

var config = {
    browsers: 'last 2 versions, ie 9'
};

/**
 * Watching files for changes
 */
gulp.task('watch', ['sass'], function() {
  browserSync.init({
    proxy: 'andco.lo'
  });

  gulp.watch(src.icons, ['icons:watch']);
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
    .pipe(prefix(config.browsers))
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

/** SVG icons */
gulp.task('icons:watch', function() {
    runSequence('icons', reload);
});

gulp.task('icons', function() {
    return gulp.src(src.icons)
        .pipe(svgSymbols({ templates: ['assets/icons/templates/icons.svg'] }))
        .pipe(rename('icons.svg'))
        .pipe(gulp.dest('assets/images/'));
});
