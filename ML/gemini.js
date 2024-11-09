const { GoogleGenerativeAI } = import("@google/generative-ai");

const genAI = new GoogleGenerativeAI("AIzaSyBIWfovuq6ZlaoY_LZLSqR7WgUBmwWvh6c");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

const prompt = "Explain how AI works";

const result = await model.generateContent(prompt);
const response = await result.response;
const text = response.text();
console.log(text);

