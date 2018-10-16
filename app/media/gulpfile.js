var gulp        = require('gulp');
var sass        = require('gulp-sass');
var cssmin      = require('gulp-clean-css');
var concat      = require('gulp-concat');
var sourcemaps  = require('gulp-sourcemaps');
var gulpIf      = require('gulp-if');

const isProd = process.env.ENV && process.env.ENV == 'prod';
const isLocal = process.env.ENV && process.env.ENV == 'loc';

console.log(process.env.ENV);

gulp.task('style', function () {
    return gulp.src('src/css/main.scss')
        .pipe(gulpIf(!isProd, sourcemaps.init()))
        .pipe(sass())
        .pipe(cssmin())
        .pipe(gulpIf(!isProd, sourcemaps.write()))
        .pipe(concat('style.css'))
        .pipe(gulp.dest('css'))
});

gulp.task('watch', function () {
    gulp.watch('src/css/**/*.scss', gulp.series('style'));
});

if (isLocal) {
    gulp.task('default', gulp.series('style', 'watch'));
} else {
    gulp.task('default', gulp.series('style'));
}

/*
* return merge(lessStream, cssStream)
        .pipe(concat(hash+'_style.min.css'))
		.pipe(cssmin())
        //.pipe(gulpIf(!isProd, sourcemaps.write()))
		.pipe(gulp.dest(files_directories[2]));
		*/

