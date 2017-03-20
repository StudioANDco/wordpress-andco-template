<!Doctype html>
<html class="no-js" <?php language_attributes() ?>>
  <head>
    <title><?php wp_title( '&middot;', true, 'right' ); ?></title>

    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="cleartype" content="on">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="canonical" href="https://www.andco.ch/">

    <meta property="og:type" content="business.business" />
    <meta property="og:site_name" content="andco"/>
    <meta property="og:locale" content="fr_FR" />

      <meta property="business:contact_data:street_address" content="Rue de l'Industrie 40" />
      <meta property="business:contact_data:locality" content="Sion" />
      <meta property="business:contact_data:postal_code" content="1950" />
      <meta property="business:contact_data:country_name" content="Suisse" />
      <meta property="place:location:latitude" content="46.227210" />
      <meta property="place:location:longitude" content="7.365095" />

    <meta property="og:title" content="andco" />
    <meta property="og:image" content="<?= get_stylesheet_directory_uri(); ?>/assets/images/facebook.png" />
    <meta property="og:url" content="https://www.andco.ch/" />
    <meta property="og:description" content="andco" />

    <link rel="apple-touch-icon" sizes="57x57" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="<?= get_stylesheet_directory_uri(); ?>/assets/favicon/apple-icon-180x180.png">
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
        <h1><a href="<?= home_url(); ?>">andco</a></h1>
    </header>

    <nav>
    </nav>

    <?php wp_nav_menu(); ?>
