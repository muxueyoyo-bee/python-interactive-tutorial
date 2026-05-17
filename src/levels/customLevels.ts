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
import customer_churn from "./custom/customer-churn";
import spam_detector from "./custom/spam-detector";
import handwrite_nn from "./custom/handwrite-nn";
import housing_predict from "./custom/housing-predict";
import color_cluster from "./custom/color-cluster";
import credit_fraud from "./custom/credit-fraud";

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
  customer_churn,
  spam_detector,
  handwrite_nn,
  housing_predict,
  color_cluster,
  credit_fraud,
];

export default customLevels;