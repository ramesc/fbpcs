# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

cmake_minimum_required(VERSION 3.10.1)
project(game)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include("common.cmake")
include("perf_tools.cmake")

# lift
add_executable(
  lift_calculator
  "fbpcs/emp_games/lift/calculator/main.cpp"
  "fbpcs/emp_games/lift/calculator/OutputMetrics.hpp"
  "fbpcs/emp_games/lift/common/GroupedLiftMetrics.h"
  "fbpcs/emp_games/lift/common/GroupedLiftMetrics.cpp"
  "fbpcs/emp_games/lift/common/LiftMetrics.h"
  "fbpcs/emp_games/lift/common/LiftMetrics.cpp"
  "fbpcs/emp_games/lift/calculator/CalculatorApp.h"
  "fbpcs/emp_games/lift/calculator/CalculatorApp.cpp"
  "fbpcs/emp_games/lift/calculator/CalculatorGame.h"
  "fbpcs/emp_games/lift/calculator/OutputMetrics.h"
  "fbpcs/emp_games/lift/calculator/InputData.cpp"
  "fbpcs/emp_games/lift/calculator/InputData.h"
  "fbpcs/emp_games/lift/calculator/CalculatorGameConfig.h"
  "fbpcs/emp_games/lift/calculator/OutputMetricsData.h"
  "fbpcs/emp_games/common/PrivateData.h"
  "fbpcs/emp_games/common/SecretSharing.h"
  "fbpcs/emp_games/common/EmpOperationUtil.h"
  "fbpcs/emp_games/common/Csv.h"
  "fbpcs/emp_games/common/Csv.cpp")
target_link_libraries(
  lift_calculator
  empgamecommon)
install(TARGETS lift_calculator DESTINATION bin)

# generic shard_aggregator
file(GLOB shard_aggregator_src
  "fbpcs/emp_games/attribution/shard_aggregator/AggMetrics.cpp",
  "fbpcs/emp_games/attribution/shard_aggregator/AggMetricsThresholdCheckers.cpp",
  "fbpcs/emp_games/attribution/shard_aggregator/ShardAggregatorApp.cpp",
  "fbpcs/emp_games/attribution/shard_aggregator/ShardAggregatorValidation.cpp",
  "fbpcs/emp_games/attribution/shard_aggregator/main.cpp"
  "fbpcs/emp_games/attribution/Aggregator.h"
  "fbpcs/emp_games/attribution/AttributionMetrics.h"
  "fbpcs/emp_games/attribution/AttributionRule.h"
  "fbpcs/emp_games/attribution/Constants.h"
  "fbpcs/emp_games/attribution/Conversion.h"
  "fbpcs/emp_games/attribution/Debug.h"
  "fbpcs/emp_games/attribution/Touchpoint.h",
  "fbpcs/emp_games/attribution/shard_aggregator/MainUtil.h",
  "fbpcs/emp_games/attribution/shard_aggregator/ShardAggregatorGame.h")
add_executable(
  shard_aggregator
  ${shard_aggregator_src})
target_link_libraries(
  shard_aggregator
  empgamecommon
  perftools)
install(TARGETS shard_aggregator DESTINATION bin)

# decoupled_attribution
file(GLOB decoupled_attribution_src
  "fbpcs/emp_games/attribution/decoupled_attribution/**.c"
  "fbpcs/emp_games/attribution/decoupled_attribution/**.cpp"
  "fbpcs/emp_games/attribution/decoupled_attribution/**.h"
  "fbpcs/emp_games/attribution/decoupled_attribution/**.hpp")
list(FILTER decoupled_attribution_src EXCLUDE REGEX ".*Test.*")
add_executable(
  decoupled_attribution_calculator
  ${decoupled_attribution_src})
target_link_libraries(
  decoupled_attribution_calculator
  empgamecommon
  perftools)
install(TARGETS decoupled_attribution_calculator DESTINATION bin)

# decoupled_aggregation
file(GLOB decoupled_aggregation_src
  "fbpcs/emp_games/attribution/decoupled_aggregation/**.c"
  "fbpcs/emp_games/attribution/decoupled_aggregation/**.cpp"
  "fbpcs/emp_games/attribution/decoupled_aggregation/**.h"
  "fbpcs/emp_games/attribution/decoupled_aggregation/metadata/**.h"
  "fbpcs/emp_games/attribution/decoupled_aggregation/**.hpp")
list(FILTER decoupled_aggregation_src EXCLUDE REGEX ".*Test.*")
add_executable(
  decoupled_aggregation_calculator
  ${decoupled_aggregation_src})
target_link_libraries(
  decoupled_aggregation_calculator
  empgamecommon
  perftools)
install(TARGETS decoupled_aggregation_calculator DESTINATION bin)

# pcf2_attribution
file(GLOB pcf2_attribution_src
  "fbpcs/emp_games/pcf2_attribution/**.c"
  "fbpcs/emp_games/pcf2_attribution/**.cpp"
  "fbpcs/emp_games/pcf2_attribution/**.h"
  "fbpcs/emp_games/pcf2_attribution/**.hpp")
list(FILTER pcf2_attribution_src EXCLUDE REGEX ".*Test.*")
add_executable(
  pcf2_attribution_calculator
  ${pcf2_attribution_src})
target_link_libraries(
  pcf2_attribution_calculator
  empgamecommon
  perftools)
install(TARGETS pcf2_attribution_calculator DESTINATION bin)

# pcf2_aggregation
file(GLOB pcf2_aggregation_src
  "fbpcs/emp_games/pcf2_aggregation/**.c"
  "fbpcs/emp_games/pcf2_aggregation/**.cpp"
  "fbpcs/emp_games/pcf2_aggregation/**.h"
  "fbpcs/emp_games/pcf2_aggregation/**.hpp")
list(FILTER pcf2_aggregation_src EXCLUDE REGEX ".*Test.*")
add_executable(
  pcf2_aggregation_calculator
  ${pcf2_aggregation_src})
target_link_libraries(
  pcf2_aggregation_calculator
  empgamecommon
  perftools)
install(TARGETS pcf2_aggregation_calculator DESTINATION bin)

# pcf2_lift
file(GLOB pcf2_lift_calculator_src
  "fbpcs/emp_games/lift/common/**.cpp"
  "fbpcs/emp_games/lift/common/**.h"
  "fbpcs/emp_games/lift/pcf2_calculator/**.cpp"
  "fbpcs/emp_games/lift/pcf2_calculator/**.h")
list(FILTER pcf2_lift_calculator_src EXCLUDE REGEX ".*Test.*")
add_executable(
  pcf2_lift_calculator
  ${pcf2_lift_calculator_src})
target_link_libraries(
  pcf2_lift_calculator
  empgamecommon
  perftools)
install(TARGETS pcf2_lift_calculator DESTINATION bin)
