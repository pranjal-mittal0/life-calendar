const finished_button = document.querySelector("#finished-input");
const birthdate = document.querySelector("#birthdateInput")
const expectancy = document.querySelector("#years")

// quiz page - for modifying age expectancy; TODO will be moved to /settings/quiz/
finished_button.addEventListener("click", function (e) {
    let bdayDate = new Date(birthdate.value);

    // they are missing data
    if (expectancy.value == "" || birthdate.value == "") {
        warningOutput(e, "Please fill out all data.");
        const error = setTimeout(warningHide, 3000);
        return;

    // birthdate is set in the future
    } else if (Date.parse(birthdate.value) > Date.now()) {
        warningOutput(e, "Please provide a valid birthdate.");
        const error = setTimeout(warningHide, 3000);

    // set an age expectancy lower than their current age
    } else if (calculateDays(bdayDate) > expectancy.value * 365) {
        warningOutput(
            e,
            "Please set your life expectancy higher or equal to your age."
        );
        const error = setTimeout(warningHide, 3000);
        
    } else {
        // TODO: move to DB for users
        localStorage.setItem("age-expectancy", expectancy.value);
        localStorage.setItem("birthday", birthdate.value);
        location.href = "/?view=months&page=1"
        e.preventDefault()
    }
});

function warningOutput(e, msg) {
    document.querySelector(".get-data").classList.remove("d-none");
    document.querySelector(".get-data").innerHTML = msg;
    e.preventDefault();
}

function warningHide() {
    document.querySelector(".get-data").classList.add("d-none");
}

function calculateDays(bday) {
    const current_day = new Date(Date.now());
    const diffTime = Math.abs(current_day - bday);
    return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
}