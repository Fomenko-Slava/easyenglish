var gulp        = require('gulp');
var sass        = require('gulp-sass');
var cssmin      = require('gulp-clean-css');
var concat      = require('gulp-concat');
var sourcemaps  = require('gulp-sourcemaps');
var gulpIf      = require('gulp-if');
var uglify 		= require('gulp-uglify');

const isProd = process.env.ENV && process.env.ENV == 'prod';
const isLocal = process.env.ENV && process.env.ENV == 'loc';

console.log(process.env.ENV);

var path = {
    src_scripts: [
        'src/js/**/*.js'
    ],
    dest_scripts: 'js'
};

gulp.task('style', function () {
    return gulp.src('src/css/main.scss')
        .pipe(gulpIf(!isProd, sourcemaps.init()))
        .pipe(sass())
        .pipe(cssmin())
        .pipe(gulpIf(!isProd, sourcemaps.write()))
        .pipe(concat('style.css'))
        .pipe(gulp.dest('css'))
});

gulp.task('scripts', function() {
	return gulp.src(path.src_scripts)
	  .pipe(concat('scripts.js'))
	  .pipe(gulp.dest(path.dest_scripts));
});

gulp.task('scripts-min', function() {
	return gulp.src(path.src_scripts)
	  .pipe(concat('scripts.min.js'))
      .pipe(uglify())
	  .pipe(gulp.dest(path.dest_scripts));
});

gulp.task('watch', function () {
    gulp.watch('src/css/**/*.scss', gulp.series('style'));
    gulp.watch('src/js/**/*.js', gulp.series('scripts'));
});

if (isLocal) {
    gulp.task('default', gulp.series('style', 'scripts', 'watch'));
} else {
    gulp.task('default', gulp.series('style', 'scripts-min'));
}

/*
* return merge(lessStream, cssStream)
        .pipe(concat(hash+'_style.min.css'))
		.pipe(cssmin())
        //.pipe(gulpIf(!isProd, sourcemaps.write()))
		.pipe(gulp.dest(files_directories[2]));
		*/

