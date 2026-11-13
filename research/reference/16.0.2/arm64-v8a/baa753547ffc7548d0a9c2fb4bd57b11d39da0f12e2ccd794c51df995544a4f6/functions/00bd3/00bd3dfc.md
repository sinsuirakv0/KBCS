# 00bd3dfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bd3dfc",
  "name": "_ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv",
  "size": 1176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11762ef5823a32da07f89ed2740a51e815f3937d879254ff11a758667341ad4f",
  "source_text_sha256": "11762ef5823a32da07f89ed2740a51e815f3937d879254ff11a758667341ad4f"
}
~~~

## 呼び出し元

- [00c5dd70](../00c5d/00c5dd70.md)

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

## 疑似コード / UTF-8 5855 bytes

~~~c

void _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv(long *param_1)

{
  if (DAT_01126948 != 0) {
    if (DAT_01126950 != '\0') {
                    /* try { // try from 00bd3e2c to 00cd3e3b has its CatchHandler @ 00bd6a18 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126950 = '\0';
    }
                    /* try { // try from 00bd3e3c to 00cd3fb7 has its CatchHandler @ 00bd09c8 */
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126948);
    DAT_01126948 = 0;
  }
  if (DAT_01126978 != 0) {
    if (DAT_01126980 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126980 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126978);
    DAT_01126978 = 0;
  }
  if (DAT_011269a8 != 0) {
    if (DAT_011269b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011269b0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011269a8);
    DAT_011269a8 = 0;
  }
  if (DAT_011269c8 != 0) {
    if (DAT_011269d0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011269d0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011269c8);
    DAT_011269c8 = 0;
  }
  if (DAT_011269e8 != 0) {
    if (DAT_011269f0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_011269f0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_011269e8);
    DAT_011269e8 = 0;
  }
  if (DAT_01126a08 != 0) {
    if (DAT_01126a10 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126a10 = '\0';
    }
                    /* try { // try from 00bd3fb8 to 00cd3fe7 has its CatchHandler @ 00bd662c */
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a08);
    DAT_01126a08 = 0;
  }
  if (DAT_01126a28 != 0) {
    if (DAT_01126a30 != '\0') {
                    /* try { // try from 00bd3ffc to 00cd4017 has its CatchHandler @ 00bd65d8 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126a30 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a28);
    DAT_01126a28 = 0;
  }
  if (DAT_01126a48 != 0) {
    if (DAT_01126a50 != '\0') {
                    /* try { // try from 00bd4044 to 00cd4073 has its CatchHandler @ 00bd6624 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126a50 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a48);
    DAT_01126a48 = 0;
  }
  if (DAT_01126a68 != 0) {
    if (DAT_01126a70 != '\0') {
                    /* try { // try from 00bd4088 to 00cd40a3 has its CatchHandler @ 00bd65d4 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126a70 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a68);
    DAT_01126a68 = 0;
  }
  if (DAT_01126a88 != 0) {
                    /* try { // try from 00bd40c8 to 00cd40f7 has its CatchHandler @ 00bd661c */
    if (DAT_01126a90 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126a90 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126a88);
    DAT_01126a88 = 0;
  }
                    /* try { // try from 00bd410c to 00cd4127 has its CatchHandler @ 00bd65d0 */
  if (DAT_01126ac8 != 0) {
    if (DAT_01126ad0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126ad0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bd414c to 00cd417b has its CatchHandler @ 00bd6614 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126ac8);
    DAT_01126ac8 = 0;
  }
  if (DAT_01126ae8 != 0) {
    if (DAT_01126af0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126af0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bd4190 to 00cd41ab has its CatchHandler @ 00bd65cc */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126ae8);
    DAT_01126ae8 = 0;
  }
  if (DAT_01126b08 != 0) {
    if (DAT_01126b10 != '\0') {
                    /* try { // try from 00bd41c0 to 00cd41ef has its CatchHandler @ 00bd660c */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126b10 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126b08);
    DAT_01126b08 = 0;
  }
  if (DAT_01126b28 != 0) {
    if (DAT_01126b30 != '\0') {
                    /* try { // try from 00bd4204 to 00cd421f has its CatchHandler @ 00bd65e8 */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126b30 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126b28);
                    /* try { // try from 00bd4234 to 00cd4263 has its CatchHandler @ 00bd6604 */
    DAT_01126b28 = 0;
  }
  if (DAT_01126aa8 != 0) {
    if (DAT_01126ab0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01126ab0 = '\0';
    }
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
                    /* try { // try from 00bd4278 to 00cd4293 has its CatchHandler @ 00bd65e4 */
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01126aa8);
    DAT_01126aa8 = 0;
  }
  return;
}

~~~
