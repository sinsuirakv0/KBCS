# 00bce2ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bce2ec",
  "name": "_ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1809b594c92d159fa08976a23ff4588d4727346f2c0768a581423bdd9b28365b",
  "source_text_sha256": "1809b594c92d159fa08976a23ff4588d4727346f2c0768a581423bdd9b28365b"
}
~~~

## 呼び出し元

- [00c5ed00](../00c5e/00c5ed00.md)

## 呼び出し先

- [00c5c000](../00c5c/00c5c000.md)

## 疑似コード / UTF-8 1746 bytes

~~~c

void _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv(long *param_1)

{
  if (DAT_011277e8 != 0) {
                    /* try { // try from 00bce314 to 00cce32b has its CatchHandler @ 00bcf9ac */
    if (DAT_011277f0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011277f0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bce334 to 00cce347 has its CatchHandler @ 00bcf950 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011277e8);
    DAT_011277e8 = 0;
  }
  if (DAT_01127890 != 0) {
    if (DAT_01127898 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01127898 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01127890);
                    /* try { // try from 00bce394 to 00cce39f has its CatchHandler @ 00bcfa08 */
    DAT_01127890 = 0;
  }
                    /* try { // try from 00bce3a0 to 00cce42b has its CatchHandler @ 00bcd634 */
  if (DAT_011278b0 != 0) {
    if (DAT_011278b8 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278b8 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278b0);
    DAT_011278b0 = 0;
  }
  if (DAT_011278d8 != 0) {
    if (DAT_011278e0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011278e0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011278d8);
                    /* try { // try from 00bce42c to 00cce437 has its CatchHandler @ 00bcf9b0 */
    DAT_011278d8 = 0;
  }
  return;
}

~~~
