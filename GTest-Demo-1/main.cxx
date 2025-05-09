#include <gtest/gtest.h>


int multiply(int a, int b) {
    return a * b;
}

TEST(GTestDemo1, multiplyTest) {
    EXPECT_EQ(multiply(2,3),6);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}


