function switchImage(number) {
    switch(number) {
        case 1:
            var replacement = document.getElementById("mini1").src;
            var original = document.getElementById("mainSlide").src;
            document.getElementById("mini1").src = original;
            document.getElementById("mainSlide").src = replacement;
            break;
        case 2:
            var replacement = document.getElementById("mini2").src;
            var original = document.getElementById("mainSlide").src;
            document.getElementById("mini2").src = original;
            document.getElementById("mainSlide").src = replacement;
            break;
        case 3:   
            var replacement = document.getElementById("mini3").src;
            var original = document.getElementById("mainSlide").src;
            document.getElementById("mini3").src = original;
            document.getElementById("mainSlide").src = replacement;
            break;
        default:
            var replacement = document.getElementById("mainSlide").src;
            document.getElementById("mainSlide").src = replacement;
            break;
    }
}