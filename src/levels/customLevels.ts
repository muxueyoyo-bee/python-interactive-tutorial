import type { LevelType } from "../level.d";

import stock_analyzer from "./custom/stock-analyzer";
import game_rpg from "./custom/game-rpg";
import weather_analyze from "./custom/weather-analyze";
import shopping_cart from "./custom/shopping-cart";
import password_check from "./custom/password-check";
import text_processor from "./custom/text-processor";
import bank_interest from "./custom/bank-interest";
import movie_spider from "./custom/movie-spider";
import todo_app from "./custom/todo-app";
import ai_text_gen from "./custom/ai-text-gen";

const customLevels: LevelType[] = [
  stock_analyzer,
  game_rpg,
  weather_analyze,
  shopping_cart,
  password_check,
  text_processor,
  bank_interest,
  movie_spider,
  todo_app,
  ai_text_gen,
];

export default customLevels;