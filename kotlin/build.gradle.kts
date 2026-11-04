plugins {
    kotlin("jvm") version "2.2.21"
}

repositories {
    mavenCentral()
}

kotlin {
    jvmToolchain(17)
}

val problem = providers.gradleProperty("problem").orElse("001-count-at-least").get()
require(problem.matches(Regex("[a-z0-9]+(?:-[a-z0-9]+)*"))) {
    "문제 이름에는 영문 소문자, 숫자, 하이픈을 사용하세요."
}
val solutionDirectory = layout.projectDirectory.dir("problems/$problem")
require(solutionDirectory.file("Solution.kt").asFile.isFile) {
    "problems/$problem/Solution.kt 파일을 찾을 수 없어요."
}

sourceSets {
    main {
        kotlin.setSrcDirs(listOf(solutionDirectory.asFile))
    }
}

tasks.register<JavaExec>("runSolution") {
    group = "practice"
    description = "선택한 문제의 Main.kt 예제를 실행합니다."
    dependsOn(tasks.named("classes"))
    classpath = sourceSets.main.get().runtimeClasspath
    mainClass.set("MainKt")
}

val checkSolution by tasks.registering(JavaExec::class) {
    group = "verification"
    description = "선택한 문제의 Check.kt 사례를 검증합니다."
    dependsOn(tasks.named("classes"))
    classpath = sourceSets.main.get().runtimeClasspath
    mainClass.set("CheckKt")
}

tasks.named("check") {
    dependsOn(checkSolution)
}
