var linear_algebra = new Array("cholesky-factorization.html","linear_algebra.html");
var differential_equations = new Array("differential_equations.html");
var machine_learning = new Array("ols-estimator-variance.html","ols-estimator.html","machine_learning.html");
var programming = new Array("programming.html");
var physics = new Array("physics.html");
var veterinary_studies = new Array("veterinary_studies.html");
function random_flashcard(flashcards) {
    var path = '<iframe src="flashcards/';
    var random_index = Math.floor(Math.random()*flashcards.length);
    path += flashcards[random_index];
    path += '" width="95%"></iframe>';
    return path;
    }