const dropdowns = [
    { btnId: 'btn1', menuId: 'dropdown1', arrowId: 'arrow1' },
    { btnId: 'btn2', menuId: 'dropdown2', arrowId: 'arrow2' }
];

dropdowns.forEach(({ btnId, menuId, arrowId }) => {
    const dropdownBtn = document.getElementById(btnId);
    const dropdownMenu = document.getElementById(menuId);
    const toggleArrow = document.getElementById(arrowId);

    // Toggle dropdown function
    const toggleDropdown = function () {
        dropdownMenu.classList.toggle("show");
        toggleArrow.classList.toggle("arrow");
    };

    // Toggle dropdown open/close when dropdown button is clicked
    dropdownBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        toggleDropdown();
    });

    // Close dropdown when dom element is clicked
    document.documentElement.addEventListener("click", function () {
        if (dropdownMenu.classList.contains("show")) {
            toggleDropdown();
        }
    });
});

