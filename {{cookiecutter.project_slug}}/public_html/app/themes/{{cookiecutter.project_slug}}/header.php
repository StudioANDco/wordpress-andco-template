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

    <meta itemprop="name" property="og:title" content="{{ cookiecutter.project_name }}" />
    <meta itemprop="image" property="og:image" content="<?= get_stylesheet_directory_uri(); ?>/assets/images/facebook.png" />
    <meta itemprop="url" property="og:url" content="https://{{ cookiecutter.project_slug.replace('_', '-') }}.ch/" />
    <meta itemprop="description" property="og:description" content="{{ cookiecutter.project_name }}" />

    <link rel="manifest" href="<?= get_stylesheet_directory_uri(); ?>/assets/site.webmanifest">
    <link rel="apple-touch-icon" href="<?= get_stylesheet_directory_uri(); ?>/assets/icon.png">

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
