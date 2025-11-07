import React, { useEffect, useState } from "react";

function RecipeList() {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/recipes/")
      .then((res) => res.json())
      .then((data) => setRecipes(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="recipe-list">
      <h2>Recipes</h2>
      {recipes.length === 0 ? (
        <p>No recipes yet!</p>
      ) : (
        recipes.map((r) => (
          <div key={r.id} className="recipe-card">
            <h3>{r.title}</h3>
            <p>{r.description}</p>
            <span>👩‍🍳 by User {r.user_id}</span>
          </div>
        ))
      )}
    </div>
  );
}

export default RecipeList;
