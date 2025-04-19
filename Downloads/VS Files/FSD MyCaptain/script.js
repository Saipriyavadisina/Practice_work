const menu = [
    {
      id: 1,
      title: "Spring Rolls",
      category: "appetizers",
      price: "$5.99",
      img: "springroll.webp",
      desc: "Crispy vegetarian rolls served with sweet chili sauce."
    },
    {
      id: 2,
      title: "Grilled Chicken",
      category: "main",
      price: "$12.99",
      img: "Grilled-Chicken.jpg",
      desc: "Juicy grilled chicken breast with herbs and garlic butter."
    },
    {
      id: 3,
      title: "Chocolate Lava Cake",
      category: "desserts",
      price: "$6.50",
      img: "chocolate-lava.webp",
      desc: "Molten chocolate center with vanilla ice cream."
    },
    {
      id: 4,
      title: "Mango Smoothie",
      category: "beverages",
      price: "$3.99",
      img: "Mango-smoothie.webp",
      desc: "Fresh mango blended with yogurt and honey."
    },
    {
      id: 5,
      title: "Pasta Alfredo",
      category: "main",
      price: "$11.50",
      img: "pasta-alfredo.jpg",
      desc: "Creamy Alfredo sauce with fettuccine pasta."
    },
  ];
  
  const menuContainer = document.getElementById('menu-items');
  const filterButtons = document.querySelectorAll('.category-btn');
  
  window.addEventListener('DOMContentLoaded', () => {
    displayMenuItems(menu);
  });
  
  filterButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const category = e.currentTarget.dataset.category;
      const filteredMenu = category === 'all' ? menu : menu.filter(item => item.category === category);
      displayMenuItems(filteredMenu);
    });
  });
  
  function displayMenuItems(menuItems) {
    let displayMenu = menuItems.map(item => {
      return `
        <div class="col-md-6 col-lg-4">
          <div class="menu-item">
            <img src="${item.img}" alt="${item.title}" />
            <div class="menu-item-body">
              <h5>${item.title}</h5>
              <p class="price">${item.price}</p>
              <p>${item.desc}</p>
            </div>
          </div>
        </div>
      `;
    }).join('');
    menuContainer.innerHTML = displayMenu;
  }
  