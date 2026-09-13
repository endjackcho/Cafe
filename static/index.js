const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>{
        if(entry.isIntersecting){
            entry.target.classList.add("show");
            observer.unobserve(entry.target)
        }
    });
});

const elements = document.querySelectorAll(".reveal");

elements.forEach((element) =>{
    observer.observe(element)
})

const buttons = document.querySelectorAll(".icon");

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        const item = button.closest(".item");

        document.querySelectorAll(".item.active").forEach((activeItem) => {
            if (activeItem !== item){
                activeItem.classList.remove("active");
            }
        });
        item.classList.toggle("active");
    });
});