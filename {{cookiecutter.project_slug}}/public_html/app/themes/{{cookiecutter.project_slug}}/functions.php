<?php
include_once 'includes/theme_setup.php';
include_once 'includes/theme_overrides.php';

add_action( 'init', 'create_taxonomies' );
function create_taxonomies() {
}

define('PREFIX', 'andco');

add_action('init', 'create_post_type');
function create_post_type() {
    register_post_type(PREFIX.'_sample',
        array(
            'labels' => array(
                'name' => __('Samples', 'template'),
                'singular_name' => __('Sample', 'template')
            ),
            'show_ui' => true,
            'capability_type' => 'page',
            'supports' => array(
                'title', 'editor', 'thumbnail', 'page-attributes'
            ),
            'menu_icon' => 'dashicons-businessman',
        )
    );
}

function get_custom_posts($name, $args = []) {
    return new WP_Query(array_merge([
        'post_type' => PREFIX.'_'.$name,
        'posts_per_page' => -1,
        'order' => 'ASC',
        'orderby' => 'menu_order'
    ], $args));
}

function samples() {
    return get_custom_posts('sample');
}
