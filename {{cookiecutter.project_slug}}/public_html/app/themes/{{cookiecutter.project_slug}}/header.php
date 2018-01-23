<!Doctype html>
<html class="no-js" <?php language_attributes() ?>>
  <head>
    <title><?php wp_title( '&middot;', true, 'right' ); ?></title>

    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta http-equiv="cleartype" content="on">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="canonical" href="https://{{ cookiecutter.project_slug.replace('_', '-') }}.ch/">

    <meta property="og:type" content="business.business" />
    <meta property="og:site_name" content="{{ cookiecutter.project_name }}"/>
    <meta property="og:locale" content="fr_FR" />

    <meta property="business:contact_data:street_address" content="Avenue du Ritz 35" />
    <meta property="business:contact_data:locality" content="Sion" />
    <meta property="business:contact_data:postal_code" content="1950" />
    <meta property="business:contact_data:country_name" content="Suisse" />
    <meta property="place:location:latitude" content="46.235885" />
    <meta property="place:location:longitude" content="7.3578723" />

    <meta property="og:title" content="{{ cookiecutter.project_name }}" />
    <meta property="og:image" content="<?= get_stylesheet_directory_uri(); ?>/assets/images/facebook.png" />
    <meta property="og:url" content="https://{{ cookiecutter.project_slug.replace('_', '-') }}.ch/" />
    <meta property="og:description" content="{{ cookiecutter.project_name }}" />

    <link rel="apple-touch-icon" href="<?= get_stylesheet_directory_uri(); ?>/assets/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="192x192"  href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/favicon-16x16.png">
    <link rel="manifest" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/manifest.json">
    <meta name="msapplication-TileColor" content="#000000">
    <meta name="msapplication-TileImage" content="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/ms-icon-144x144.png">

    <meta name="msapplication-navbutton-color" content="#000000">
    <meta name="theme-color" content="#000000">
    <meta name="apple-mobile-web-app-status-bar-style" content="#000000">

    <?php wp_head(); ?>
  </head>

  <body <?php body_class(); ?>>
    <header>
        <h1><a href="<?= home_url(); ?>">{{ cookiecutter.project_name }}</a></h1>
    </header>

    <nav>
        <?php wp_nav_menu(); ?>
    </nav>
