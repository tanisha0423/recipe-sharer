import React, { useState } from "react";

const CreateRecipe = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [ingredients, setIngredients] = useState("");
  const [instructions, setInstructions] = useState("");
  const [userId, setUserId] = useState(""); // Linked user ID
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const recipeData = {
      title,
      description,
      ingredients,
      instructions,
    };

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/recipes/?user_id=${userId}`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(recipeData),
        }
      );

      if (!response.ok) throw new Error("Failed to create recipe");

      setMessage("✅ Recipe created successfully!");
      setTitle("");
      setDescription("");
      setIngredients("");
      setInstructions("");
      setUserId("");
    } catch (error) {
      setMessage("❌ Error creating recipe: " + error.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🍳 Create a New Recipe</h2>

      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
          style={styles.input}
        />
        <input
          type="text"
          placeholder="Recipe Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          style={styles.input}
        />
        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={styles.textarea}
        ></textarea>
        <textarea
          placeholder="Ingredients"
          value={ingredients}
          onChange={(e) => setIngredients(e.target.value)}
          style={styles.textarea}
        ></textarea>
        <textarea
          placeholder="Instructions"
          value={instructions}
          onChange={(e) => setInstructions(e.target.value)}
          style={styles.textarea}
        ></textarea>

        <button type="submit" style={styles.button}>
          Create Recipe
        </button>
      </form>

      {message && <p style={styles.message}>{message}</p>}
    </div>
  );
};

const styles = {
  container: {
    background: "#f8f9fa",
    borderRadius: "20px",
    padding: "30px",
    width: "400px",
    margin: "50px auto",
    boxShadow: "0 4px 10px rgba(0,0,0,0.2)",
    textAlign: "center",
  },
  title: {
    color: "#333",
    fontFamily: "Poppins, sans-serif",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },
  input: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
  },
  textarea: {
    padding: "10px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    resize: "none",
    height: "60px",
  },
  button: {
    backgroundColor: "#ff7b7b",
    color: "white",
    border: "none",
    padding: "10px",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold",
    marginTop: "10px",
  },
  message: {
    marginTop: "15px",
    color: "#555",
  },
};

export default CreateRecipe;
