import React from "react";
import RegisterUser from "./components/RegisterUser";
import RecipeList from "./components/RecipeList";
import CreateRecipe from "./components/CreateRecipe";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1>🍰 Recipe Sharing Platform</h1>
      <RegisterUser />
      <CreateRecipe />
      <RecipeList />
    </div>
  );
}

export default App;
