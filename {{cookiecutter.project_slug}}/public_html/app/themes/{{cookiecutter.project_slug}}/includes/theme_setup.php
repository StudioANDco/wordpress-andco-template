<?php
/**
 * Enable some WordPress functionnalites
 */

add_theme_support( 'post-thumbnails' );

add_theme_support( 'html5', array(
  'search-form',
  'comment-form',
  'comment-list',
  'gallery',
  'caption'
) );

// Load dedicated stylesheet into WordPress text editor
add_editor_style( get_template_directory_uri() . '/assets/stylesheets/editor.css' );


/**
 * Load locales
 */

load_theme_textdomain( 'template', TEMPLATEPATH . '/languages' );


/**
 * Register Sidebars
 */

register_sidebar( array(
  'id'            => 'primary',
  'name'          => __( 'Primary sidebar', 'template' ),
  'before_widget' => '<div id="%1$s" class="widget %2$s">',
  'after_widget'  => '</div>',
  'before_title'  => '<h3>',
  'after_title'   => '</h3>'
) );


/**
 * Register Menus
 */

function theme_menus() {
  register_nav_menu( 'primary', __( 'Primary navigation', 'template' ) );
}
add_action( 'after_setup_theme', 'theme_menus' );


/**
 * Enqueue required scripts and styles
 */

function theme_assets() {
  wp_register_script( 'theme', get_template_directory_uri() . '/javascripts/production.min.js', array( 'jquery' ) );
  wp_enqueue_script( 'theme' );

  wp_register_style( 'theme', get_template_directory_uri() . '/assets/stylesheets/theme.css' );
  wp_enqueue_style( 'theme' );

  wp_register_style( 'fonts', '//fonts.googleapis.com/css?family=Open+Sans' );
  wp_enqueue_style( 'fonts' );
}
add_action( 'wp_enqueue_scripts', 'theme_assets' );
