<?php get_header() ?>

<section class="samples"  id="samples">
    <header>
        <h1>Samples</h1>
    </header>
<?php
$query = informations();
if ($query->have_posts()) {
    while($query->have_posts()) {
        $query->the_post();
?>
    <article>
        <div>
            <header>
                <h1><?php echo get_the_title(); ?></h1>
                <img src="<?php echo get_the_post_thumbnail_url() ?>">
            </header>
            <?php echo get_the_content(); ?>
        </div>
    </article>
<?php
    }
}
?></section>

<?php get_footer() ?>

