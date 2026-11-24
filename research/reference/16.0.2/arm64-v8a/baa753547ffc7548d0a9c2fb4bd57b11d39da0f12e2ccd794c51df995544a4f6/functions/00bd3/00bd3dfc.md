# 00bd3dfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd3d60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3d60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0083.md#compare-b9b461f905427aa439e3f5fc894fc5ba)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0095.md#compare-b4eaca46e297073f814215ed96d93366)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
