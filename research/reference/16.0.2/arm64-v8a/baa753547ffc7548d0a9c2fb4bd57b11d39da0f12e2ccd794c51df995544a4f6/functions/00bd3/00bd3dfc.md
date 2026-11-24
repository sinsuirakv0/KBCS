# 00bd3dfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd3d60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd3/00bd3d60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0083.md#compare-b9b461f905427aa439e3f5fc894fc5ba)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd4df0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd4/00bd4df0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0083.md#compare-b4eaca46e297073f814215ed96d93366)
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
  "source_text_sha256": "11762ef5823a32da07f89ed2740a51e815f3937d879254ff11a758667341ad4f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd3dfc",
        "00bd4293"
      ]
    ],
    "bytes_sha256": "b2ba8add5eceea591d79f67ce245c52b7782542ebac7baceea1ef754ac591f60",
    "instruction_count": 294,
    "instruction_bytes": 1176,
    "body_bytes": 1176,
    "indirect": 30,
    "unresolved": 30
  }
}
~~~

## 呼び出し元

- [00c5dd70](../00c5d/00c5dd70.md)

## 呼び出し先

- [00c5b030](../00c5b/00c5b030.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd3dfc"></a> `00bd3dfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd3e00"></a> `00bd3e00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd3e04"></a> `00bd3e04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd3e08"></a> `00bd3e08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bd3e0c"></a> `00bd3e0c` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3e10"></a> `00bd3e10` | `81 a6 44 f9` | ldr x1,[x20, #0x948] | `FALL_THROUGH`
<a id="insn-00bd3e14"></a> `00bd3e14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd3e18"></a> `00bd3e18` | `21 02 00 b4` | cbz x1,0x00bd3e5c | `CONDITIONAL_JUMP`
<a id="insn-00bd3e1c"></a> `00bd3e1c` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3e20"></a> `00bd3e20` | `a8 42 65 39` | ldrb w8,[x21, #0x950] | `FALL_THROUGH`
<a id="insn-00bd3e24"></a> `00bd3e24` | `c8 00 00 34` | cbz w8,0x00bd3e3c | `CONDITIONAL_JUMP`
<a id="insn-00bd3e28"></a> `00bd3e28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3e2c"></a> `00bd3e2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3e30"></a> `00bd3e30` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3e34"></a> `00bd3e34` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3e38"></a> `00bd3e38` | `bf 42 25 39` | strb wzr,[x21, #0x950] | `FALL_THROUGH`
<a id="insn-00bd3e3c"></a> `00bd3e3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3e40"></a> `00bd3e40` | `7c 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3e44"></a> `00bd3e44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3e48"></a> `00bd3e48` | `81 a6 44 f9` | ldr x1,[x20, #0x948] | `FALL_THROUGH`
<a id="insn-00bd3e4c"></a> `00bd3e4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3e50"></a> `00bd3e50` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3e54"></a> `00bd3e54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3e58"></a> `00bd3e58` | `9f a6 04 f9` | str xzr,[x20, #0x948] | `FALL_THROUGH`
<a id="insn-00bd3e5c"></a> `00bd3e5c` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3e60"></a> `00bd3e60` | `81 be 44 f9` | ldr x1,[x20, #0x978] | `FALL_THROUGH`
<a id="insn-00bd3e64"></a> `00bd3e64` | `21 02 00 b4` | cbz x1,0x00bd3ea8 | `CONDITIONAL_JUMP`
<a id="insn-00bd3e68"></a> `00bd3e68` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3e6c"></a> `00bd3e6c` | `a8 02 66 39` | ldrb w8,[x21, #0x980] | `FALL_THROUGH`
<a id="insn-00bd3e70"></a> `00bd3e70` | `c8 00 00 34` | cbz w8,0x00bd3e88 | `CONDITIONAL_JUMP`
<a id="insn-00bd3e74"></a> `00bd3e74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3e78"></a> `00bd3e78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3e7c"></a> `00bd3e7c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3e80"></a> `00bd3e80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3e84"></a> `00bd3e84` | `bf 02 26 39` | strb wzr,[x21, #0x980] | `FALL_THROUGH`
<a id="insn-00bd3e88"></a> `00bd3e88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3e8c"></a> `00bd3e8c` | `69 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3e90"></a> `00bd3e90` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3e94"></a> `00bd3e94` | `81 be 44 f9` | ldr x1,[x20, #0x978] | `FALL_THROUGH`
<a id="insn-00bd3e98"></a> `00bd3e98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3e9c"></a> `00bd3e9c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3ea0"></a> `00bd3ea0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3ea4"></a> `00bd3ea4` | `9f be 04 f9` | str xzr,[x20, #0x978] | `FALL_THROUGH`
<a id="insn-00bd3ea8"></a> `00bd3ea8` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3eac"></a> `00bd3eac` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bd3eb0"></a> `00bd3eb0` | `21 02 00 b4` | cbz x1,0x00bd3ef4 | `CONDITIONAL_JUMP`
<a id="insn-00bd3eb4"></a> `00bd3eb4` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3eb8"></a> `00bd3eb8` | `a8 c2 66 39` | ldrb w8,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00bd3ebc"></a> `00bd3ebc` | `c8 00 00 34` | cbz w8,0x00bd3ed4 | `CONDITIONAL_JUMP`
<a id="insn-00bd3ec0"></a> `00bd3ec0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3ec4"></a> `00bd3ec4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3ec8"></a> `00bd3ec8` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3ecc"></a> `00bd3ecc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3ed0"></a> `00bd3ed0` | `bf c2 26 39` | strb wzr,[x21, #0x9b0] | `FALL_THROUGH`
<a id="insn-00bd3ed4"></a> `00bd3ed4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3ed8"></a> `00bd3ed8` | `56 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3edc"></a> `00bd3edc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3ee0"></a> `00bd3ee0` | `81 d6 44 f9` | ldr x1,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bd3ee4"></a> `00bd3ee4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3ee8"></a> `00bd3ee8` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3eec"></a> `00bd3eec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3ef0"></a> `00bd3ef0` | `9f d6 04 f9` | str xzr,[x20, #0x9a8] | `FALL_THROUGH`
<a id="insn-00bd3ef4"></a> `00bd3ef4` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3ef8"></a> `00bd3ef8` | `81 e6 44 f9` | ldr x1,[x20, #0x9c8] | `FALL_THROUGH`
<a id="insn-00bd3efc"></a> `00bd3efc` | `21 02 00 b4` | cbz x1,0x00bd3f40 | `CONDITIONAL_JUMP`
<a id="insn-00bd3f00"></a> `00bd3f00` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3f04"></a> `00bd3f04` | `a8 42 67 39` | ldrb w8,[x21, #0x9d0] | `FALL_THROUGH`
<a id="insn-00bd3f08"></a> `00bd3f08` | `c8 00 00 34` | cbz w8,0x00bd3f20 | `CONDITIONAL_JUMP`
<a id="insn-00bd3f0c"></a> `00bd3f0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3f10"></a> `00bd3f10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3f14"></a> `00bd3f14` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3f18"></a> `00bd3f18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3f1c"></a> `00bd3f1c` | `bf 42 27 39` | strb wzr,[x21, #0x9d0] | `FALL_THROUGH`
<a id="insn-00bd3f20"></a> `00bd3f20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3f24"></a> `00bd3f24` | `43 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3f28"></a> `00bd3f28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3f2c"></a> `00bd3f2c` | `81 e6 44 f9` | ldr x1,[x20, #0x9c8] | `FALL_THROUGH`
<a id="insn-00bd3f30"></a> `00bd3f30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3f34"></a> `00bd3f34` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3f38"></a> `00bd3f38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3f3c"></a> `00bd3f3c` | `9f e6 04 f9` | str xzr,[x20, #0x9c8] | `FALL_THROUGH`
<a id="insn-00bd3f40"></a> `00bd3f40` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3f44"></a> `00bd3f44` | `81 f6 44 f9` | ldr x1,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd3f48"></a> `00bd3f48` | `21 02 00 b4` | cbz x1,0x00bd3f8c | `CONDITIONAL_JUMP`
<a id="insn-00bd3f4c"></a> `00bd3f4c` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3f50"></a> `00bd3f50` | `a8 c2 67 39` | ldrb w8,[x21, #0x9f0] | `FALL_THROUGH`
<a id="insn-00bd3f54"></a> `00bd3f54` | `c8 00 00 34` | cbz w8,0x00bd3f6c | `CONDITIONAL_JUMP`
<a id="insn-00bd3f58"></a> `00bd3f58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3f5c"></a> `00bd3f5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3f60"></a> `00bd3f60` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3f64"></a> `00bd3f64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3f68"></a> `00bd3f68` | `bf c2 27 39` | strb wzr,[x21, #0x9f0] | `FALL_THROUGH`
<a id="insn-00bd3f6c"></a> `00bd3f6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3f70"></a> `00bd3f70` | `30 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3f74"></a> `00bd3f74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3f78"></a> `00bd3f78` | `81 f6 44 f9` | ldr x1,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd3f7c"></a> `00bd3f7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3f80"></a> `00bd3f80` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3f84"></a> `00bd3f84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3f88"></a> `00bd3f88` | `9f f6 04 f9` | str xzr,[x20, #0x9e8] | `FALL_THROUGH`
<a id="insn-00bd3f8c"></a> `00bd3f8c` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3f90"></a> `00bd3f90` | `81 06 45 f9` | ldr x1,[x20, #0xa08] | `FALL_THROUGH`
<a id="insn-00bd3f94"></a> `00bd3f94` | `21 02 00 b4` | cbz x1,0x00bd3fd8 | `CONDITIONAL_JUMP`
<a id="insn-00bd3f98"></a> `00bd3f98` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3f9c"></a> `00bd3f9c` | `a8 42 68 39` | ldrb w8,[x21, #0xa10] | `FALL_THROUGH`
<a id="insn-00bd3fa0"></a> `00bd3fa0` | `c8 00 00 34` | cbz w8,0x00bd3fb8 | `CONDITIONAL_JUMP`
<a id="insn-00bd3fa4"></a> `00bd3fa4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3fa8"></a> `00bd3fa8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3fac"></a> `00bd3fac` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3fb0"></a> `00bd3fb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3fb4"></a> `00bd3fb4` | `bf 42 28 39` | strb wzr,[x21, #0xa10] | `FALL_THROUGH`
<a id="insn-00bd3fb8"></a> `00bd3fb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3fbc"></a> `00bd3fbc` | `1d 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd3fc0"></a> `00bd3fc0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3fc4"></a> `00bd3fc4` | `81 06 45 f9` | ldr x1,[x20, #0xa08] | `FALL_THROUGH`
<a id="insn-00bd3fc8"></a> `00bd3fc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3fcc"></a> `00bd3fcc` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd3fd0"></a> `00bd3fd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd3fd4"></a> `00bd3fd4` | `9f 06 05 f9` | str xzr,[x20, #0xa08] | `FALL_THROUGH`
<a id="insn-00bd3fd8"></a> `00bd3fd8` | `94 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3fdc"></a> `00bd3fdc` | `81 16 45 f9` | ldr x1,[x20, #0xa28] | `FALL_THROUGH`
<a id="insn-00bd3fe0"></a> `00bd3fe0` | `21 02 00 b4` | cbz x1,0x00bd4024 | `CONDITIONAL_JUMP`
<a id="insn-00bd3fe4"></a> `00bd3fe4` | `95 2a 00 f0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd3fe8"></a> `00bd3fe8` | `a8 c2 68 39` | ldrb w8,[x21, #0xa30] | `FALL_THROUGH`
<a id="insn-00bd3fec"></a> `00bd3fec` | `c8 00 00 34` | cbz w8,0x00bd4004 | `CONDITIONAL_JUMP`
<a id="insn-00bd3ff0"></a> `00bd3ff0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd3ff4"></a> `00bd3ff4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd3ff8"></a> `00bd3ff8` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd3ffc"></a> `00bd3ffc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4000"></a> `00bd4000` | `bf c2 28 39` | strb wzr,[x21, #0xa30] | `FALL_THROUGH`
<a id="insn-00bd4004"></a> `00bd4004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4008"></a> `00bd4008` | `0a 1c 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd400c"></a> `00bd400c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4010"></a> `00bd4010` | `81 16 45 f9` | ldr x1,[x20, #0xa28] | `FALL_THROUGH`
<a id="insn-00bd4014"></a> `00bd4014` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4018"></a> `00bd4018` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd401c"></a> `00bd401c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4020"></a> `00bd4020` | `9f 16 05 f9` | str xzr,[x20, #0xa28] | `FALL_THROUGH`
<a id="insn-00bd4024"></a> `00bd4024` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4028"></a> `00bd4028` | `81 26 45 f9` | ldr x1,[x20, #0xa48] | `FALL_THROUGH`
<a id="insn-00bd402c"></a> `00bd402c` | `21 02 00 b4` | cbz x1,0x00bd4070 | `CONDITIONAL_JUMP`
<a id="insn-00bd4030"></a> `00bd4030` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4034"></a> `00bd4034` | `a8 42 69 39` | ldrb w8,[x21, #0xa50] | `FALL_THROUGH`
<a id="insn-00bd4038"></a> `00bd4038` | `c8 00 00 34` | cbz w8,0x00bd4050 | `CONDITIONAL_JUMP`
<a id="insn-00bd403c"></a> `00bd403c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4040"></a> `00bd4040` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4044"></a> `00bd4044` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd4048"></a> `00bd4048` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd404c"></a> `00bd404c` | `bf 42 29 39` | strb wzr,[x21, #0xa50] | `FALL_THROUGH`
<a id="insn-00bd4050"></a> `00bd4050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4054"></a> `00bd4054` | `f7 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4058"></a> `00bd4058` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd405c"></a> `00bd405c` | `81 26 45 f9` | ldr x1,[x20, #0xa48] | `FALL_THROUGH`
<a id="insn-00bd4060"></a> `00bd4060` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4064"></a> `00bd4064` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd4068"></a> `00bd4068` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd406c"></a> `00bd406c` | `9f 26 05 f9` | str xzr,[x20, #0xa48] | `FALL_THROUGH`
<a id="insn-00bd4070"></a> `00bd4070` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4074"></a> `00bd4074` | `81 36 45 f9` | ldr x1,[x20, #0xa68] | `FALL_THROUGH`
<a id="insn-00bd4078"></a> `00bd4078` | `21 02 00 b4` | cbz x1,0x00bd40bc | `CONDITIONAL_JUMP`
<a id="insn-00bd407c"></a> `00bd407c` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4080"></a> `00bd4080` | `a8 c2 69 39` | ldrb w8,[x21, #0xa70] | `FALL_THROUGH`
<a id="insn-00bd4084"></a> `00bd4084` | `c8 00 00 34` | cbz w8,0x00bd409c | `CONDITIONAL_JUMP`
<a id="insn-00bd4088"></a> `00bd4088` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd408c"></a> `00bd408c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4090"></a> `00bd4090` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd4094"></a> `00bd4094` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4098"></a> `00bd4098` | `bf c2 29 39` | strb wzr,[x21, #0xa70] | `FALL_THROUGH`
<a id="insn-00bd409c"></a> `00bd409c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd40a0"></a> `00bd40a0` | `e4 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd40a4"></a> `00bd40a4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd40a8"></a> `00bd40a8` | `81 36 45 f9` | ldr x1,[x20, #0xa68] | `FALL_THROUGH`
<a id="insn-00bd40ac"></a> `00bd40ac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd40b0"></a> `00bd40b0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd40b4"></a> `00bd40b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd40b8"></a> `00bd40b8` | `9f 36 05 f9` | str xzr,[x20, #0xa68] | `FALL_THROUGH`
<a id="insn-00bd40bc"></a> `00bd40bc` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd40c0"></a> `00bd40c0` | `81 46 45 f9` | ldr x1,[x20, #0xa88] | `FALL_THROUGH`
<a id="insn-00bd40c4"></a> `00bd40c4` | `21 02 00 b4` | cbz x1,0x00bd4108 | `CONDITIONAL_JUMP`
<a id="insn-00bd40c8"></a> `00bd40c8` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd40cc"></a> `00bd40cc` | `a8 42 6a 39` | ldrb w8,[x21, #0xa90] | `FALL_THROUGH`
<a id="insn-00bd40d0"></a> `00bd40d0` | `c8 00 00 34` | cbz w8,0x00bd40e8 | `CONDITIONAL_JUMP`
<a id="insn-00bd40d4"></a> `00bd40d4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd40d8"></a> `00bd40d8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd40dc"></a> `00bd40dc` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd40e0"></a> `00bd40e0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd40e4"></a> `00bd40e4` | `bf 42 2a 39` | strb wzr,[x21, #0xa90] | `FALL_THROUGH`
<a id="insn-00bd40e8"></a> `00bd40e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd40ec"></a> `00bd40ec` | `d1 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd40f0"></a> `00bd40f0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd40f4"></a> `00bd40f4` | `81 46 45 f9` | ldr x1,[x20, #0xa88] | `FALL_THROUGH`
<a id="insn-00bd40f8"></a> `00bd40f8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd40fc"></a> `00bd40fc` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd4100"></a> `00bd4100` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4104"></a> `00bd4104` | `9f 46 05 f9` | str xzr,[x20, #0xa88] | `FALL_THROUGH`
<a id="insn-00bd4108"></a> `00bd4108` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd410c"></a> `00bd410c` | `81 66 45 f9` | ldr x1,[x20, #0xac8] | `FALL_THROUGH`
<a id="insn-00bd4110"></a> `00bd4110` | `21 02 00 b4` | cbz x1,0x00bd4154 | `CONDITIONAL_JUMP`
<a id="insn-00bd4114"></a> `00bd4114` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4118"></a> `00bd4118` | `a8 42 6b 39` | ldrb w8,[x21, #0xad0] | `FALL_THROUGH`
<a id="insn-00bd411c"></a> `00bd411c` | `c8 00 00 34` | cbz w8,0x00bd4134 | `CONDITIONAL_JUMP`
<a id="insn-00bd4120"></a> `00bd4120` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4124"></a> `00bd4124` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4128"></a> `00bd4128` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd412c"></a> `00bd412c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4130"></a> `00bd4130` | `bf 42 2b 39` | strb wzr,[x21, #0xad0] | `FALL_THROUGH`
<a id="insn-00bd4134"></a> `00bd4134` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4138"></a> `00bd4138` | `be 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd413c"></a> `00bd413c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4140"></a> `00bd4140` | `81 66 45 f9` | ldr x1,[x20, #0xac8] | `FALL_THROUGH`
<a id="insn-00bd4144"></a> `00bd4144` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4148"></a> `00bd4148` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd414c"></a> `00bd414c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4150"></a> `00bd4150` | `9f 66 05 f9` | str xzr,[x20, #0xac8] | `FALL_THROUGH`
<a id="insn-00bd4154"></a> `00bd4154` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4158"></a> `00bd4158` | `81 76 45 f9` | ldr x1,[x20, #0xae8] | `FALL_THROUGH`
<a id="insn-00bd415c"></a> `00bd415c` | `21 02 00 b4` | cbz x1,0x00bd41a0 | `CONDITIONAL_JUMP`
<a id="insn-00bd4160"></a> `00bd4160` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4164"></a> `00bd4164` | `a8 c2 6b 39` | ldrb w8,[x21, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bd4168"></a> `00bd4168` | `c8 00 00 34` | cbz w8,0x00bd4180 | `CONDITIONAL_JUMP`
<a id="insn-00bd416c"></a> `00bd416c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4170"></a> `00bd4170` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4174"></a> `00bd4174` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd4178"></a> `00bd4178` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd417c"></a> `00bd417c` | `bf c2 2b 39` | strb wzr,[x21, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bd4180"></a> `00bd4180` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4184"></a> `00bd4184` | `ab 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4188"></a> `00bd4188` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd418c"></a> `00bd418c` | `81 76 45 f9` | ldr x1,[x20, #0xae8] | `FALL_THROUGH`
<a id="insn-00bd4190"></a> `00bd4190` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4194"></a> `00bd4194` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd4198"></a> `00bd4198` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd419c"></a> `00bd419c` | `9f 76 05 f9` | str xzr,[x20, #0xae8] | `FALL_THROUGH`
<a id="insn-00bd41a0"></a> `00bd41a0` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd41a4"></a> `00bd41a4` | `81 86 45 f9` | ldr x1,[x20, #0xb08] | `FALL_THROUGH`
<a id="insn-00bd41a8"></a> `00bd41a8` | `21 02 00 b4` | cbz x1,0x00bd41ec | `CONDITIONAL_JUMP`
<a id="insn-00bd41ac"></a> `00bd41ac` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd41b0"></a> `00bd41b0` | `a8 42 6c 39` | ldrb w8,[x21, #0xb10] | `FALL_THROUGH`
<a id="insn-00bd41b4"></a> `00bd41b4` | `c8 00 00 34` | cbz w8,0x00bd41cc | `CONDITIONAL_JUMP`
<a id="insn-00bd41b8"></a> `00bd41b8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd41bc"></a> `00bd41bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd41c0"></a> `00bd41c0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd41c4"></a> `00bd41c4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd41c8"></a> `00bd41c8` | `bf 42 2c 39` | strb wzr,[x21, #0xb10] | `FALL_THROUGH`
<a id="insn-00bd41cc"></a> `00bd41cc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd41d0"></a> `00bd41d0` | `98 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd41d4"></a> `00bd41d4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd41d8"></a> `00bd41d8` | `81 86 45 f9` | ldr x1,[x20, #0xb08] | `FALL_THROUGH`
<a id="insn-00bd41dc"></a> `00bd41dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd41e0"></a> `00bd41e0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd41e4"></a> `00bd41e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd41e8"></a> `00bd41e8` | `9f 86 05 f9` | str xzr,[x20, #0xb08] | `FALL_THROUGH`
<a id="insn-00bd41ec"></a> `00bd41ec` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd41f0"></a> `00bd41f0` | `81 96 45 f9` | ldr x1,[x20, #0xb28] | `FALL_THROUGH`
<a id="insn-00bd41f4"></a> `00bd41f4` | `21 02 00 b4` | cbz x1,0x00bd4238 | `CONDITIONAL_JUMP`
<a id="insn-00bd41f8"></a> `00bd41f8` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd41fc"></a> `00bd41fc` | `a8 c2 6c 39` | ldrb w8,[x21, #0xb30] | `FALL_THROUGH`
<a id="insn-00bd4200"></a> `00bd4200` | `c8 00 00 34` | cbz w8,0x00bd4218 | `CONDITIONAL_JUMP`
<a id="insn-00bd4204"></a> `00bd4204` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4208"></a> `00bd4208` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd420c"></a> `00bd420c` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd4210"></a> `00bd4210` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4214"></a> `00bd4214` | `bf c2 2c 39` | strb wzr,[x21, #0xb30] | `FALL_THROUGH`
<a id="insn-00bd4218"></a> `00bd4218` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd421c"></a> `00bd421c` | `85 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4220"></a> `00bd4220` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4224"></a> `00bd4224` | `81 96 45 f9` | ldr x1,[x20, #0xb28] | `FALL_THROUGH`
<a id="insn-00bd4228"></a> `00bd4228` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd422c"></a> `00bd422c` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd4230"></a> `00bd4230` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4234"></a> `00bd4234` | `9f 96 05 f9` | str xzr,[x20, #0xb28] | `FALL_THROUGH`
<a id="insn-00bd4238"></a> `00bd4238` | `94 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd423c"></a> `00bd423c` | `81 56 45 f9` | ldr x1,[x20, #0xaa8] | `FALL_THROUGH`
<a id="insn-00bd4240"></a> `00bd4240` | `21 02 00 b4` | cbz x1,0x00bd4284 | `CONDITIONAL_JUMP`
<a id="insn-00bd4244"></a> `00bd4244` | `95 2a 00 d0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd4248"></a> `00bd4248` | `a8 c2 6a 39` | ldrb w8,[x21, #0xab0] | `FALL_THROUGH`
<a id="insn-00bd424c"></a> `00bd424c` | `c8 00 00 34` | cbz w8,0x00bd4264 | `CONDITIONAL_JUMP`
<a id="insn-00bd4250"></a> `00bd4250` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4254"></a> `00bd4254` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4258"></a> `00bd4258` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00bd425c"></a> `00bd425c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4260"></a> `00bd4260` | `bf c2 2a 39` | strb wzr,[x21, #0xab0] | `FALL_THROUGH`
<a id="insn-00bd4264"></a> `00bd4264` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4268"></a> `00bd4268` | `72 1b 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bd426c"></a> `00bd426c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bd4270"></a> `00bd4270` | `81 56 45 f9` | ldr x1,[x20, #0xaa8] | `FALL_THROUGH`
<a id="insn-00bd4274"></a> `00bd4274` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd4278"></a> `00bd4278` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd427c"></a> `00bd427c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4280"></a> `00bd4280` | `9f 56 05 f9` | str xzr,[x20, #0xaa8] | `FALL_THROUGH`
<a id="insn-00bd4284"></a> `00bd4284` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd4288"></a> `00bd4288` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd428c"></a> `00bd428c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd4290"></a> `00bd4290` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd3dfc`](#insn-00bd3dfc) 範囲 `[['00bd3dfc', '00bd3e1b']]`
  - `CONDITIONAL_JUMP` [`00bd3e18`](#insn-00bd3e18) → [`00bd3e5c`](#insn-00bd3e5c)
  - `FALL_THROUGH` [`00bd3e18`](#insn-00bd3e18) → [`00bd3e1c`](#insn-00bd3e1c)
- ブロック [`00bd3e1c`](#insn-00bd3e1c) 範囲 `[['00bd3e1c', '00bd3e27']]`
  - `CONDITIONAL_JUMP` [`00bd3e24`](#insn-00bd3e24) → [`00bd3e3c`](#insn-00bd3e3c)
  - `FALL_THROUGH` [`00bd3e24`](#insn-00bd3e24) → [`00bd3e28`](#insn-00bd3e28)
- ブロック [`00bd3e28`](#insn-00bd3e28) 範囲 `[['00bd3e28', '00bd3e2b']]`
  - `FALL_THROUGH` [`00bd3e28`](#insn-00bd3e28) → [`00bd3e2c`](#insn-00bd3e2c)
- ブロック [`00bd3e2c`](#insn-00bd3e2c) 範囲 `[['00bd3e2c', '00bd3e3b']]`
  - `FALL_THROUGH` [`00bd3e38`](#insn-00bd3e38) → [`00bd3e3c`](#insn-00bd3e3c)
- ブロック [`00bd3e3c`](#insn-00bd3e3c) 範囲 `[['00bd3e3c', '00bd3e5b']]`
  - `FALL_THROUGH` [`00bd3e58`](#insn-00bd3e58) → [`00bd3e5c`](#insn-00bd3e5c)
- ブロック [`00bd3e5c`](#insn-00bd3e5c) 範囲 `[['00bd3e5c', '00bd3e67']]`
  - `CONDITIONAL_JUMP` [`00bd3e64`](#insn-00bd3e64) → [`00bd3ea8`](#insn-00bd3ea8)
  - `FALL_THROUGH` [`00bd3e64`](#insn-00bd3e64) → [`00bd3e68`](#insn-00bd3e68)
- ブロック [`00bd3e68`](#insn-00bd3e68) 範囲 `[['00bd3e68', '00bd3e73']]`
  - `CONDITIONAL_JUMP` [`00bd3e70`](#insn-00bd3e70) → [`00bd3e88`](#insn-00bd3e88)
  - `FALL_THROUGH` [`00bd3e70`](#insn-00bd3e70) → [`00bd3e74`](#insn-00bd3e74)
- ブロック [`00bd3e74`](#insn-00bd3e74) 範囲 `[['00bd3e74', '00bd3e87']]`
  - `FALL_THROUGH` [`00bd3e84`](#insn-00bd3e84) → [`00bd3e88`](#insn-00bd3e88)
- ブロック [`00bd3e88`](#insn-00bd3e88) 範囲 `[['00bd3e88', '00bd3ea7']]`
  - `FALL_THROUGH` [`00bd3ea4`](#insn-00bd3ea4) → [`00bd3ea8`](#insn-00bd3ea8)
- ブロック [`00bd3ea8`](#insn-00bd3ea8) 範囲 `[['00bd3ea8', '00bd3eb3']]`
  - `CONDITIONAL_JUMP` [`00bd3eb0`](#insn-00bd3eb0) → [`00bd3ef4`](#insn-00bd3ef4)
  - `FALL_THROUGH` [`00bd3eb0`](#insn-00bd3eb0) → [`00bd3eb4`](#insn-00bd3eb4)
- ブロック [`00bd3eb4`](#insn-00bd3eb4) 範囲 `[['00bd3eb4', '00bd3ebf']]`
  - `CONDITIONAL_JUMP` [`00bd3ebc`](#insn-00bd3ebc) → [`00bd3ed4`](#insn-00bd3ed4)
  - `FALL_THROUGH` [`00bd3ebc`](#insn-00bd3ebc) → [`00bd3ec0`](#insn-00bd3ec0)
- ブロック [`00bd3ec0`](#insn-00bd3ec0) 範囲 `[['00bd3ec0', '00bd3ed3']]`
  - `FALL_THROUGH` [`00bd3ed0`](#insn-00bd3ed0) → [`00bd3ed4`](#insn-00bd3ed4)
- ブロック [`00bd3ed4`](#insn-00bd3ed4) 範囲 `[['00bd3ed4', '00bd3ef3']]`
  - `FALL_THROUGH` [`00bd3ef0`](#insn-00bd3ef0) → [`00bd3ef4`](#insn-00bd3ef4)
- ブロック [`00bd3ef4`](#insn-00bd3ef4) 範囲 `[['00bd3ef4', '00bd3eff']]`
  - `CONDITIONAL_JUMP` [`00bd3efc`](#insn-00bd3efc) → [`00bd3f40`](#insn-00bd3f40)
  - `FALL_THROUGH` [`00bd3efc`](#insn-00bd3efc) → [`00bd3f00`](#insn-00bd3f00)
- ブロック [`00bd3f00`](#insn-00bd3f00) 範囲 `[['00bd3f00', '00bd3f0b']]`
  - `CONDITIONAL_JUMP` [`00bd3f08`](#insn-00bd3f08) → [`00bd3f20`](#insn-00bd3f20)
  - `FALL_THROUGH` [`00bd3f08`](#insn-00bd3f08) → [`00bd3f0c`](#insn-00bd3f0c)
- ブロック [`00bd3f0c`](#insn-00bd3f0c) 範囲 `[['00bd3f0c', '00bd3f1f']]`
  - `FALL_THROUGH` [`00bd3f1c`](#insn-00bd3f1c) → [`00bd3f20`](#insn-00bd3f20)
- ブロック [`00bd3f20`](#insn-00bd3f20) 範囲 `[['00bd3f20', '00bd3f3f']]`
  - `FALL_THROUGH` [`00bd3f3c`](#insn-00bd3f3c) → [`00bd3f40`](#insn-00bd3f40)
- ブロック [`00bd3f40`](#insn-00bd3f40) 範囲 `[['00bd3f40', '00bd3f4b']]`
  - `CONDITIONAL_JUMP` [`00bd3f48`](#insn-00bd3f48) → [`00bd3f8c`](#insn-00bd3f8c)
  - `FALL_THROUGH` [`00bd3f48`](#insn-00bd3f48) → [`00bd3f4c`](#insn-00bd3f4c)
- ブロック [`00bd3f4c`](#insn-00bd3f4c) 範囲 `[['00bd3f4c', '00bd3f57']]`
  - `CONDITIONAL_JUMP` [`00bd3f54`](#insn-00bd3f54) → [`00bd3f6c`](#insn-00bd3f6c)
  - `FALL_THROUGH` [`00bd3f54`](#insn-00bd3f54) → [`00bd3f58`](#insn-00bd3f58)
- ブロック [`00bd3f58`](#insn-00bd3f58) 範囲 `[['00bd3f58', '00bd3f6b']]`
  - `FALL_THROUGH` [`00bd3f68`](#insn-00bd3f68) → [`00bd3f6c`](#insn-00bd3f6c)
- ブロック [`00bd3f6c`](#insn-00bd3f6c) 範囲 `[['00bd3f6c', '00bd3f8b']]`
  - `FALL_THROUGH` [`00bd3f88`](#insn-00bd3f88) → [`00bd3f8c`](#insn-00bd3f8c)
- ブロック [`00bd3f8c`](#insn-00bd3f8c) 範囲 `[['00bd3f8c', '00bd3f97']]`
  - `CONDITIONAL_JUMP` [`00bd3f94`](#insn-00bd3f94) → [`00bd3fd8`](#insn-00bd3fd8)
  - `FALL_THROUGH` [`00bd3f94`](#insn-00bd3f94) → [`00bd3f98`](#insn-00bd3f98)
- ブロック [`00bd3f98`](#insn-00bd3f98) 範囲 `[['00bd3f98', '00bd3fa3']]`
  - `CONDITIONAL_JUMP` [`00bd3fa0`](#insn-00bd3fa0) → [`00bd3fb8`](#insn-00bd3fb8)
  - `FALL_THROUGH` [`00bd3fa0`](#insn-00bd3fa0) → [`00bd3fa4`](#insn-00bd3fa4)
- ブロック [`00bd3fa4`](#insn-00bd3fa4) 範囲 `[['00bd3fa4', '00bd3fb7']]`
  - `FALL_THROUGH` [`00bd3fb4`](#insn-00bd3fb4) → [`00bd3fb8`](#insn-00bd3fb8)
- ブロック [`00bd3fb8`](#insn-00bd3fb8) 範囲 `[['00bd3fb8', '00bd3fd7']]`
  - `FALL_THROUGH` [`00bd3fd4`](#insn-00bd3fd4) → [`00bd3fd8`](#insn-00bd3fd8)
- ブロック [`00bd3fd8`](#insn-00bd3fd8) 範囲 `[['00bd3fd8', '00bd3fe3']]`
  - `CONDITIONAL_JUMP` [`00bd3fe0`](#insn-00bd3fe0) → [`00bd4024`](#insn-00bd4024)
  - `FALL_THROUGH` [`00bd3fe0`](#insn-00bd3fe0) → [`00bd3fe4`](#insn-00bd3fe4)
- ブロック [`00bd3fe4`](#insn-00bd3fe4) 範囲 `[['00bd3fe4', '00bd3fef']]`
  - `CONDITIONAL_JUMP` [`00bd3fec`](#insn-00bd3fec) → [`00bd4004`](#insn-00bd4004)
  - `FALL_THROUGH` [`00bd3fec`](#insn-00bd3fec) → [`00bd3ff0`](#insn-00bd3ff0)
- ブロック [`00bd3ff0`](#insn-00bd3ff0) 範囲 `[['00bd3ff0', '00bd3ffb']]`
  - `FALL_THROUGH` [`00bd3ff8`](#insn-00bd3ff8) → [`00bd3ffc`](#insn-00bd3ffc)
- ブロック [`00bd3ffc`](#insn-00bd3ffc) 範囲 `[['00bd3ffc', '00bd4003']]`
  - `FALL_THROUGH` [`00bd4000`](#insn-00bd4000) → [`00bd4004`](#insn-00bd4004)
- ブロック [`00bd4004`](#insn-00bd4004) 範囲 `[['00bd4004', '00bd4023']]`
  - `FALL_THROUGH` [`00bd4020`](#insn-00bd4020) → [`00bd4024`](#insn-00bd4024)
- ブロック [`00bd4024`](#insn-00bd4024) 範囲 `[['00bd4024', '00bd402f']]`
  - `CONDITIONAL_JUMP` [`00bd402c`](#insn-00bd402c) → [`00bd4070`](#insn-00bd4070)
  - `FALL_THROUGH` [`00bd402c`](#insn-00bd402c) → [`00bd4030`](#insn-00bd4030)
- ブロック [`00bd4030`](#insn-00bd4030) 範囲 `[['00bd4030', '00bd403b']]`
  - `CONDITIONAL_JUMP` [`00bd4038`](#insn-00bd4038) → [`00bd4050`](#insn-00bd4050)
  - `FALL_THROUGH` [`00bd4038`](#insn-00bd4038) → [`00bd403c`](#insn-00bd403c)
- ブロック [`00bd403c`](#insn-00bd403c) 範囲 `[['00bd403c', '00bd4043']]`
  - `FALL_THROUGH` [`00bd4040`](#insn-00bd4040) → [`00bd4044`](#insn-00bd4044)
- ブロック [`00bd4044`](#insn-00bd4044) 範囲 `[['00bd4044', '00bd404f']]`
  - `FALL_THROUGH` [`00bd404c`](#insn-00bd404c) → [`00bd4050`](#insn-00bd4050)
- ブロック [`00bd4050`](#insn-00bd4050) 範囲 `[['00bd4050', '00bd406f']]`
  - `FALL_THROUGH` [`00bd406c`](#insn-00bd406c) → [`00bd4070`](#insn-00bd4070)
- ブロック [`00bd4070`](#insn-00bd4070) 範囲 `[['00bd4070', '00bd407b']]`
  - `CONDITIONAL_JUMP` [`00bd4078`](#insn-00bd4078) → [`00bd40bc`](#insn-00bd40bc)
  - `FALL_THROUGH` [`00bd4078`](#insn-00bd4078) → [`00bd407c`](#insn-00bd407c)
- ブロック [`00bd407c`](#insn-00bd407c) 範囲 `[['00bd407c', '00bd4087']]`
  - `CONDITIONAL_JUMP` [`00bd4084`](#insn-00bd4084) → [`00bd409c`](#insn-00bd409c)
  - `FALL_THROUGH` [`00bd4084`](#insn-00bd4084) → [`00bd4088`](#insn-00bd4088)
- ブロック [`00bd4088`](#insn-00bd4088) 範囲 `[['00bd4088', '00bd409b']]`
  - `FALL_THROUGH` [`00bd4098`](#insn-00bd4098) → [`00bd409c`](#insn-00bd409c)
- ブロック [`00bd409c`](#insn-00bd409c) 範囲 `[['00bd409c', '00bd40bb']]`
  - `FALL_THROUGH` [`00bd40b8`](#insn-00bd40b8) → [`00bd40bc`](#insn-00bd40bc)
- ブロック [`00bd40bc`](#insn-00bd40bc) 範囲 `[['00bd40bc', '00bd40c7']]`
  - `CONDITIONAL_JUMP` [`00bd40c4`](#insn-00bd40c4) → [`00bd4108`](#insn-00bd4108)
  - `FALL_THROUGH` [`00bd40c4`](#insn-00bd40c4) → [`00bd40c8`](#insn-00bd40c8)
- ブロック [`00bd40c8`](#insn-00bd40c8) 範囲 `[['00bd40c8', '00bd40d3']]`
  - `CONDITIONAL_JUMP` [`00bd40d0`](#insn-00bd40d0) → [`00bd40e8`](#insn-00bd40e8)
  - `FALL_THROUGH` [`00bd40d0`](#insn-00bd40d0) → [`00bd40d4`](#insn-00bd40d4)
- ブロック [`00bd40d4`](#insn-00bd40d4) 範囲 `[['00bd40d4', '00bd40e7']]`
  - `FALL_THROUGH` [`00bd40e4`](#insn-00bd40e4) → [`00bd40e8`](#insn-00bd40e8)
- ブロック [`00bd40e8`](#insn-00bd40e8) 範囲 `[['00bd40e8', '00bd4107']]`
  - `FALL_THROUGH` [`00bd4104`](#insn-00bd4104) → [`00bd4108`](#insn-00bd4108)
- ブロック [`00bd4108`](#insn-00bd4108) 範囲 `[['00bd4108', '00bd410b']]`
  - `FALL_THROUGH` [`00bd4108`](#insn-00bd4108) → [`00bd410c`](#insn-00bd410c)
- ブロック [`00bd410c`](#insn-00bd410c) 範囲 `[['00bd410c', '00bd4113']]`
  - `CONDITIONAL_JUMP` [`00bd4110`](#insn-00bd4110) → [`00bd4154`](#insn-00bd4154)
  - `FALL_THROUGH` [`00bd4110`](#insn-00bd4110) → [`00bd4114`](#insn-00bd4114)
- ブロック [`00bd4114`](#insn-00bd4114) 範囲 `[['00bd4114', '00bd411f']]`
  - `CONDITIONAL_JUMP` [`00bd411c`](#insn-00bd411c) → [`00bd4134`](#insn-00bd4134)
  - `FALL_THROUGH` [`00bd411c`](#insn-00bd411c) → [`00bd4120`](#insn-00bd4120)
- ブロック [`00bd4120`](#insn-00bd4120) 範囲 `[['00bd4120', '00bd4133']]`
  - `FALL_THROUGH` [`00bd4130`](#insn-00bd4130) → [`00bd4134`](#insn-00bd4134)
- ブロック [`00bd4134`](#insn-00bd4134) 範囲 `[['00bd4134', '00bd414b']]`
  - `FALL_THROUGH` [`00bd4148`](#insn-00bd4148) → [`00bd414c`](#insn-00bd414c)
- ブロック [`00bd414c`](#insn-00bd414c) 範囲 `[['00bd414c', '00bd4153']]`
  - `FALL_THROUGH` [`00bd4150`](#insn-00bd4150) → [`00bd4154`](#insn-00bd4154)
- ブロック [`00bd4154`](#insn-00bd4154) 範囲 `[['00bd4154', '00bd415f']]`
  - `CONDITIONAL_JUMP` [`00bd415c`](#insn-00bd415c) → [`00bd41a0`](#insn-00bd41a0)
  - `FALL_THROUGH` [`00bd415c`](#insn-00bd415c) → [`00bd4160`](#insn-00bd4160)
- ブロック [`00bd4160`](#insn-00bd4160) 範囲 `[['00bd4160', '00bd416b']]`
  - `CONDITIONAL_JUMP` [`00bd4168`](#insn-00bd4168) → [`00bd4180`](#insn-00bd4180)
  - `FALL_THROUGH` [`00bd4168`](#insn-00bd4168) → [`00bd416c`](#insn-00bd416c)
- ブロック [`00bd416c`](#insn-00bd416c) 範囲 `[['00bd416c', '00bd417f']]`
  - `FALL_THROUGH` [`00bd417c`](#insn-00bd417c) → [`00bd4180`](#insn-00bd4180)
- ブロック [`00bd4180`](#insn-00bd4180) 範囲 `[['00bd4180', '00bd418f']]`
  - `FALL_THROUGH` [`00bd418c`](#insn-00bd418c) → [`00bd4190`](#insn-00bd4190)
- ブロック [`00bd4190`](#insn-00bd4190) 範囲 `[['00bd4190', '00bd419f']]`
  - `FALL_THROUGH` [`00bd419c`](#insn-00bd419c) → [`00bd41a0`](#insn-00bd41a0)
- ブロック [`00bd41a0`](#insn-00bd41a0) 範囲 `[['00bd41a0', '00bd41ab']]`
  - `CONDITIONAL_JUMP` [`00bd41a8`](#insn-00bd41a8) → [`00bd41ec`](#insn-00bd41ec)
  - `FALL_THROUGH` [`00bd41a8`](#insn-00bd41a8) → [`00bd41ac`](#insn-00bd41ac)
- ブロック [`00bd41ac`](#insn-00bd41ac) 範囲 `[['00bd41ac', '00bd41b7']]`
  - `CONDITIONAL_JUMP` [`00bd41b4`](#insn-00bd41b4) → [`00bd41cc`](#insn-00bd41cc)
  - `FALL_THROUGH` [`00bd41b4`](#insn-00bd41b4) → [`00bd41b8`](#insn-00bd41b8)
- ブロック [`00bd41b8`](#insn-00bd41b8) 範囲 `[['00bd41b8', '00bd41bf']]`
  - `FALL_THROUGH` [`00bd41bc`](#insn-00bd41bc) → [`00bd41c0`](#insn-00bd41c0)
- ブロック [`00bd41c0`](#insn-00bd41c0) 範囲 `[['00bd41c0', '00bd41cb']]`
  - `FALL_THROUGH` [`00bd41c8`](#insn-00bd41c8) → [`00bd41cc`](#insn-00bd41cc)
- ブロック [`00bd41cc`](#insn-00bd41cc) 範囲 `[['00bd41cc', '00bd41eb']]`
  - `FALL_THROUGH` [`00bd41e8`](#insn-00bd41e8) → [`00bd41ec`](#insn-00bd41ec)
- ブロック [`00bd41ec`](#insn-00bd41ec) 範囲 `[['00bd41ec', '00bd41f7']]`
  - `CONDITIONAL_JUMP` [`00bd41f4`](#insn-00bd41f4) → [`00bd4238`](#insn-00bd4238)
  - `FALL_THROUGH` [`00bd41f4`](#insn-00bd41f4) → [`00bd41f8`](#insn-00bd41f8)
- ブロック [`00bd41f8`](#insn-00bd41f8) 範囲 `[['00bd41f8', '00bd4203']]`
  - `CONDITIONAL_JUMP` [`00bd4200`](#insn-00bd4200) → [`00bd4218`](#insn-00bd4218)
  - `FALL_THROUGH` [`00bd4200`](#insn-00bd4200) → [`00bd4204`](#insn-00bd4204)
- ブロック [`00bd4204`](#insn-00bd4204) 範囲 `[['00bd4204', '00bd4217']]`
  - `FALL_THROUGH` [`00bd4214`](#insn-00bd4214) → [`00bd4218`](#insn-00bd4218)
- ブロック [`00bd4218`](#insn-00bd4218) 範囲 `[['00bd4218', '00bd4233']]`
  - `FALL_THROUGH` [`00bd4230`](#insn-00bd4230) → [`00bd4234`](#insn-00bd4234)
- ブロック [`00bd4234`](#insn-00bd4234) 範囲 `[['00bd4234', '00bd4237']]`
  - `FALL_THROUGH` [`00bd4234`](#insn-00bd4234) → [`00bd4238`](#insn-00bd4238)
- ブロック [`00bd4238`](#insn-00bd4238) 範囲 `[['00bd4238', '00bd4243']]`
  - `CONDITIONAL_JUMP` [`00bd4240`](#insn-00bd4240) → [`00bd4284`](#insn-00bd4284)
  - `FALL_THROUGH` [`00bd4240`](#insn-00bd4240) → [`00bd4244`](#insn-00bd4244)
- ブロック [`00bd4244`](#insn-00bd4244) 範囲 `[['00bd4244', '00bd424f']]`
  - `CONDITIONAL_JUMP` [`00bd424c`](#insn-00bd424c) → [`00bd4264`](#insn-00bd4264)
  - `FALL_THROUGH` [`00bd424c`](#insn-00bd424c) → [`00bd4250`](#insn-00bd4250)
- ブロック [`00bd4250`](#insn-00bd4250) 範囲 `[['00bd4250', '00bd4263']]`
  - `FALL_THROUGH` [`00bd4260`](#insn-00bd4260) → [`00bd4264`](#insn-00bd4264)
- ブロック [`00bd4264`](#insn-00bd4264) 範囲 `[['00bd4264', '00bd4277']]`
  - `FALL_THROUGH` [`00bd4274`](#insn-00bd4274) → [`00bd4278`](#insn-00bd4278)
- ブロック [`00bd4278`](#insn-00bd4278) 範囲 `[['00bd4278', '00bd4283']]`
  - `FALL_THROUGH` [`00bd4280`](#insn-00bd4280) → [`00bd4284`](#insn-00bd4284)
- ブロック [`00bd4284`](#insn-00bd4284) 範囲 `[['00bd4284', '00bd4293']]`

## 命令位置別の参照

- [`00bd3dfc`](#insn-00bd3dfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e00`](#insn-00bd3e00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e04`](#insn-00bd3e04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e10`](#insn-00bd3e10) → `01126948`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3e18`](#insn-00bd3e18) → [`00bd3e5c`](#insn-00bd3e5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e20`](#insn-00bd3e20) → `01126950`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3e24`](#insn-00bd3e24) → [`00bd3e3c`](#insn-00bd3e3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e38`](#insn-00bd3e38) → `01126950`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3e40`](#insn-00bd3e40) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e48`](#insn-00bd3e48) → `01126948`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3e58`](#insn-00bd3e58) → `01126948`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3e60`](#insn-00bd3e60) → `01126978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3e64`](#insn-00bd3e64) → [`00bd3ea8`](#insn-00bd3ea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e6c`](#insn-00bd3e6c) → `01126980`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3e70`](#insn-00bd3e70) → [`00bd3e88`](#insn-00bd3e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e84`](#insn-00bd3e84) → `01126980`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3e8c`](#insn-00bd3e8c) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3e94`](#insn-00bd3e94) → `01126978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3ea4`](#insn-00bd3ea4) → `01126978`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3eac`](#insn-00bd3eac) → `011269a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3eb0`](#insn-00bd3eb0) → [`00bd3ef4`](#insn-00bd3ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3eb8`](#insn-00bd3eb8) → `011269b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3ebc`](#insn-00bd3ebc) → [`00bd3ed4`](#insn-00bd3ed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3ed0`](#insn-00bd3ed0) → `011269b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3ed8`](#insn-00bd3ed8) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3ee0`](#insn-00bd3ee0) → `011269a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3ef0`](#insn-00bd3ef0) → `011269a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3ef8`](#insn-00bd3ef8) → `011269c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3efc`](#insn-00bd3efc) → [`00bd3f40`](#insn-00bd3f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f04`](#insn-00bd3f04) → `011269d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3f08`](#insn-00bd3f08) → [`00bd3f20`](#insn-00bd3f20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f1c`](#insn-00bd3f1c) → `011269d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3f24`](#insn-00bd3f24) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f2c`](#insn-00bd3f2c) → `011269c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f3c`](#insn-00bd3f3c) → `011269c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f44`](#insn-00bd3f44) → `011269e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f48`](#insn-00bd3f48) → [`00bd3f8c`](#insn-00bd3f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f50`](#insn-00bd3f50) → `011269f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3f54`](#insn-00bd3f54) → [`00bd3f6c`](#insn-00bd3f6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f68`](#insn-00bd3f68) → `011269f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3f70`](#insn-00bd3f70) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f78`](#insn-00bd3f78) → `011269e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f88`](#insn-00bd3f88) → `011269e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f90`](#insn-00bd3f90) → `01126a08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3f94`](#insn-00bd3f94) → [`00bd3fd8`](#insn-00bd3fd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3f9c`](#insn-00bd3f9c) → `01126a10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3fa0`](#insn-00bd3fa0) → [`00bd3fb8`](#insn-00bd3fb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3fb4`](#insn-00bd3fb4) → `01126a10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3fbc`](#insn-00bd3fbc) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd3fc4`](#insn-00bd3fc4) → `01126a08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3fd4`](#insn-00bd3fd4) → `01126a08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3fdc`](#insn-00bd3fdc) → `01126a28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd3fe0`](#insn-00bd3fe0) → [`00bd4024`](#insn-00bd4024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd3fe8`](#insn-00bd3fe8) → `01126a30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd3fec`](#insn-00bd3fec) → [`00bd4004`](#insn-00bd4004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4000`](#insn-00bd4000) → `01126a30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4008`](#insn-00bd4008) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd4010`](#insn-00bd4010) → `01126a28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4020`](#insn-00bd4020) → `01126a28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4028`](#insn-00bd4028) → `01126a48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd402c`](#insn-00bd402c) → [`00bd4070`](#insn-00bd4070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4034`](#insn-00bd4034) → `01126a50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4038`](#insn-00bd4038) → [`00bd4050`](#insn-00bd4050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd404c`](#insn-00bd404c) → `01126a50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4054`](#insn-00bd4054) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd405c`](#insn-00bd405c) → `01126a48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd406c`](#insn-00bd406c) → `01126a48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4074`](#insn-00bd4074) → `01126a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4078`](#insn-00bd4078) → [`00bd40bc`](#insn-00bd40bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4080`](#insn-00bd4080) → `01126a70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4084`](#insn-00bd4084) → [`00bd409c`](#insn-00bd409c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4098`](#insn-00bd4098) → `01126a70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd40a0`](#insn-00bd40a0) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd40a8`](#insn-00bd40a8) → `01126a68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd40b8`](#insn-00bd40b8) → `01126a68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd40c0`](#insn-00bd40c0) → `01126a88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd40c4`](#insn-00bd40c4) → [`00bd4108`](#insn-00bd4108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd40cc`](#insn-00bd40cc) → `01126a90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd40d0`](#insn-00bd40d0) → [`00bd40e8`](#insn-00bd40e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd40e4`](#insn-00bd40e4) → `01126a90`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd40ec`](#insn-00bd40ec) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd40f4`](#insn-00bd40f4) → `01126a88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4104`](#insn-00bd4104) → `01126a88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd410c`](#insn-00bd410c) → `01126ac8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4110`](#insn-00bd4110) → [`00bd4154`](#insn-00bd4154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4118`](#insn-00bd4118) → `01126ad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd411c`](#insn-00bd411c) → [`00bd4134`](#insn-00bd4134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4130`](#insn-00bd4130) → `01126ad0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4138`](#insn-00bd4138) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd4140`](#insn-00bd4140) → `01126ac8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4150`](#insn-00bd4150) → `01126ac8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4158`](#insn-00bd4158) → `01126ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd415c`](#insn-00bd415c) → [`00bd41a0`](#insn-00bd41a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4164`](#insn-00bd4164) → `01126af0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4168`](#insn-00bd4168) → [`00bd4180`](#insn-00bd4180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd417c`](#insn-00bd417c) → `01126af0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4184`](#insn-00bd4184) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd418c`](#insn-00bd418c) → `01126ae8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd419c`](#insn-00bd419c) → `01126ae8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd41a4`](#insn-00bd41a4) → `01126b08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd41a8`](#insn-00bd41a8) → [`00bd41ec`](#insn-00bd41ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd41b0`](#insn-00bd41b0) → `01126b10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd41b4`](#insn-00bd41b4) → [`00bd41cc`](#insn-00bd41cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd41c8`](#insn-00bd41c8) → `01126b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd41d0`](#insn-00bd41d0) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd41d8`](#insn-00bd41d8) → `01126b08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd41e8`](#insn-00bd41e8) → `01126b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd41f0`](#insn-00bd41f0) → `01126b28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd41f4`](#insn-00bd41f4) → [`00bd4238`](#insn-00bd4238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd41fc`](#insn-00bd41fc) → `01126b30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4200`](#insn-00bd4200) → [`00bd4218`](#insn-00bd4218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4214`](#insn-00bd4214) → `01126b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd421c`](#insn-00bd421c) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd4224`](#insn-00bd4224) → `01126b28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4234`](#insn-00bd4234) → `01126b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd423c`](#insn-00bd423c) → `01126aa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4240`](#insn-00bd4240) → [`00bd4284`](#insn-00bd4284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4248`](#insn-00bd4248) → `01126ab0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd424c`](#insn-00bd424c) → [`00bd4264`](#insn-00bd4264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4260`](#insn-00bd4260) → `01126ab0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bd4268`](#insn-00bd4268) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bd4270`](#insn-00bd4270) → `01126aa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4280`](#insn-00bd4280) → `01126aa8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd4284`](#insn-00bd4284) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4288`](#insn-00bd4288) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd3dfc`](#insn-00bd3dfc)

~~~json
{
  "source": "00bd3dfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e00`](#insn-00bd3e00)

~~~json
{
  "source": "00bd3e00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e04`](#insn-00bd3e04)

~~~json
{
  "source": "00bd3e04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e10`](#insn-00bd3e10)

~~~json
{
  "source": "00bd3e10",
  "target": "01126948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126948",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e18`](#insn-00bd3e18)

~~~json
{
  "source": "00bd3e18",
  "target": "00bd3e5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e20`](#insn-00bd3e20)

~~~json
{
  "source": "00bd3e20",
  "target": "01126950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126950",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e24`](#insn-00bd3e24)

~~~json
{
  "source": "00bd3e24",
  "target": "00bd3e3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e38`](#insn-00bd3e38)

~~~json
{
  "source": "00bd3e38",
  "target": "01126950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126950",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e40`](#insn-00bd3e40)

~~~json
{
  "source": "00bd3e40",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3e48`](#insn-00bd3e48)

~~~json
{
  "source": "00bd3e48",
  "target": "01126948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126948",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e58`](#insn-00bd3e58)

~~~json
{
  "source": "00bd3e58",
  "target": "01126948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126948",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e60`](#insn-00bd3e60)

~~~json
{
  "source": "00bd3e60",
  "target": "01126978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e64`](#insn-00bd3e64)

~~~json
{
  "source": "00bd3e64",
  "target": "00bd3ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e6c`](#insn-00bd3e6c)

~~~json
{
  "source": "00bd3e6c",
  "target": "01126980",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126980",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e70`](#insn-00bd3e70)

~~~json
{
  "source": "00bd3e70",
  "target": "00bd3e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3e84`](#insn-00bd3e84)

~~~json
{
  "source": "00bd3e84",
  "target": "01126980",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126980",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3e8c`](#insn-00bd3e8c)

~~~json
{
  "source": "00bd3e8c",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3e94`](#insn-00bd3e94)

~~~json
{
  "source": "00bd3e94",
  "target": "01126978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3ea4`](#insn-00bd3ea4)

~~~json
{
  "source": "00bd3ea4",
  "target": "01126978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3eac`](#insn-00bd3eac)

~~~json
{
  "source": "00bd3eac",
  "target": "011269a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3eb0`](#insn-00bd3eb0)

~~~json
{
  "source": "00bd3eb0",
  "target": "00bd3ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3eb8`](#insn-00bd3eb8)

~~~json
{
  "source": "00bd3eb8",
  "target": "011269b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3ebc`](#insn-00bd3ebc)

~~~json
{
  "source": "00bd3ebc",
  "target": "00bd3ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3ed0`](#insn-00bd3ed0)

~~~json
{
  "source": "00bd3ed0",
  "target": "011269b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3ed8`](#insn-00bd3ed8)

~~~json
{
  "source": "00bd3ed8",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3ee0`](#insn-00bd3ee0)

~~~json
{
  "source": "00bd3ee0",
  "target": "011269a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3ef0`](#insn-00bd3ef0)

~~~json
{
  "source": "00bd3ef0",
  "target": "011269a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3ef8`](#insn-00bd3ef8)

~~~json
{
  "source": "00bd3ef8",
  "target": "011269c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3efc`](#insn-00bd3efc)

~~~json
{
  "source": "00bd3efc",
  "target": "00bd3f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f04`](#insn-00bd3f04)

~~~json
{
  "source": "00bd3f04",
  "target": "011269d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f08`](#insn-00bd3f08)

~~~json
{
  "source": "00bd3f08",
  "target": "00bd3f20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f1c`](#insn-00bd3f1c)

~~~json
{
  "source": "00bd3f1c",
  "target": "011269d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f24`](#insn-00bd3f24)

~~~json
{
  "source": "00bd3f24",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3f2c`](#insn-00bd3f2c)

~~~json
{
  "source": "00bd3f2c",
  "target": "011269c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f3c`](#insn-00bd3f3c)

~~~json
{
  "source": "00bd3f3c",
  "target": "011269c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f44`](#insn-00bd3f44)

~~~json
{
  "source": "00bd3f44",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f48`](#insn-00bd3f48)

~~~json
{
  "source": "00bd3f48",
  "target": "00bd3f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f50`](#insn-00bd3f50)

~~~json
{
  "source": "00bd3f50",
  "target": "011269f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f54`](#insn-00bd3f54)

~~~json
{
  "source": "00bd3f54",
  "target": "00bd3f6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f68`](#insn-00bd3f68)

~~~json
{
  "source": "00bd3f68",
  "target": "011269f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269f0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f70`](#insn-00bd3f70)

~~~json
{
  "source": "00bd3f70",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3f78`](#insn-00bd3f78)

~~~json
{
  "source": "00bd3f78",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f88`](#insn-00bd3f88)

~~~json
{
  "source": "00bd3f88",
  "target": "011269e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f90`](#insn-00bd3f90)

~~~json
{
  "source": "00bd3f90",
  "target": "01126a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3f94`](#insn-00bd3f94)

~~~json
{
  "source": "00bd3f94",
  "target": "00bd3fd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3f9c`](#insn-00bd3f9c)

~~~json
{
  "source": "00bd3f9c",
  "target": "01126a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a10",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3fa0`](#insn-00bd3fa0)

~~~json
{
  "source": "00bd3fa0",
  "target": "00bd3fb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3fb4`](#insn-00bd3fb4)

~~~json
{
  "source": "00bd3fb4",
  "target": "01126a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a10",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3fbc`](#insn-00bd3fbc)

~~~json
{
  "source": "00bd3fbc",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd3fc4`](#insn-00bd3fc4)

~~~json
{
  "source": "00bd3fc4",
  "target": "01126a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3fd4`](#insn-00bd3fd4)

~~~json
{
  "source": "00bd3fd4",
  "target": "01126a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3fdc`](#insn-00bd3fdc)

~~~json
{
  "source": "00bd3fdc",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3fe0`](#insn-00bd3fe0)

~~~json
{
  "source": "00bd3fe0",
  "target": "00bd4024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd3fe8`](#insn-00bd3fe8)

~~~json
{
  "source": "00bd3fe8",
  "target": "01126a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd3fec`](#insn-00bd3fec)

~~~json
{
  "source": "00bd3fec",
  "target": "00bd4004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4000`](#insn-00bd4000)

~~~json
{
  "source": "00bd4000",
  "target": "01126a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4008`](#insn-00bd4008)

~~~json
{
  "source": "00bd4008",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4010`](#insn-00bd4010)

~~~json
{
  "source": "00bd4010",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4020`](#insn-00bd4020)

~~~json
{
  "source": "00bd4020",
  "target": "01126a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4028`](#insn-00bd4028)

~~~json
{
  "source": "00bd4028",
  "target": "01126a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd402c`](#insn-00bd402c)

~~~json
{
  "source": "00bd402c",
  "target": "00bd4070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4034`](#insn-00bd4034)

~~~json
{
  "source": "00bd4034",
  "target": "01126a50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a50",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4038`](#insn-00bd4038)

~~~json
{
  "source": "00bd4038",
  "target": "00bd4050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd404c`](#insn-00bd404c)

~~~json
{
  "source": "00bd404c",
  "target": "01126a50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a50",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4054`](#insn-00bd4054)

~~~json
{
  "source": "00bd4054",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd405c`](#insn-00bd405c)

~~~json
{
  "source": "00bd405c",
  "target": "01126a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd406c`](#insn-00bd406c)

~~~json
{
  "source": "00bd406c",
  "target": "01126a48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4074`](#insn-00bd4074)

~~~json
{
  "source": "00bd4074",
  "target": "01126a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4078`](#insn-00bd4078)

~~~json
{
  "source": "00bd4078",
  "target": "00bd40bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4080`](#insn-00bd4080)

~~~json
{
  "source": "00bd4080",
  "target": "01126a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a70",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4084`](#insn-00bd4084)

~~~json
{
  "source": "00bd4084",
  "target": "00bd409c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4098`](#insn-00bd4098)

~~~json
{
  "source": "00bd4098",
  "target": "01126a70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a70",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd40a0`](#insn-00bd40a0)

~~~json
{
  "source": "00bd40a0",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd40a8`](#insn-00bd40a8)

~~~json
{
  "source": "00bd40a8",
  "target": "01126a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd40b8`](#insn-00bd40b8)

~~~json
{
  "source": "00bd40b8",
  "target": "01126a68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd40c0`](#insn-00bd40c0)

~~~json
{
  "source": "00bd40c0",
  "target": "01126a88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd40c4`](#insn-00bd40c4)

~~~json
{
  "source": "00bd40c4",
  "target": "00bd4108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd40cc`](#insn-00bd40cc)

~~~json
{
  "source": "00bd40cc",
  "target": "01126a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd40d0`](#insn-00bd40d0)

~~~json
{
  "source": "00bd40d0",
  "target": "00bd40e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd40e4`](#insn-00bd40e4)

~~~json
{
  "source": "00bd40e4",
  "target": "01126a90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a90",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd40ec`](#insn-00bd40ec)

~~~json
{
  "source": "00bd40ec",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd40f4`](#insn-00bd40f4)

~~~json
{
  "source": "00bd40f4",
  "target": "01126a88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4104`](#insn-00bd4104)

~~~json
{
  "source": "00bd4104",
  "target": "01126a88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126a88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd410c`](#insn-00bd410c)

~~~json
{
  "source": "00bd410c",
  "target": "01126ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ac8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4110`](#insn-00bd4110)

~~~json
{
  "source": "00bd4110",
  "target": "00bd4154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4118`](#insn-00bd4118)

~~~json
{
  "source": "00bd4118",
  "target": "01126ad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ad0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd411c`](#insn-00bd411c)

~~~json
{
  "source": "00bd411c",
  "target": "00bd4134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4130`](#insn-00bd4130)

~~~json
{
  "source": "00bd4130",
  "target": "01126ad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ad0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4138`](#insn-00bd4138)

~~~json
{
  "source": "00bd4138",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4140`](#insn-00bd4140)

~~~json
{
  "source": "00bd4140",
  "target": "01126ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ac8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4150`](#insn-00bd4150)

~~~json
{
  "source": "00bd4150",
  "target": "01126ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ac8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4158`](#insn-00bd4158)

~~~json
{
  "source": "00bd4158",
  "target": "01126ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd415c`](#insn-00bd415c)

~~~json
{
  "source": "00bd415c",
  "target": "00bd41a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4164`](#insn-00bd4164)

~~~json
{
  "source": "00bd4164",
  "target": "01126af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4168`](#insn-00bd4168)

~~~json
{
  "source": "00bd4168",
  "target": "00bd4180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd417c`](#insn-00bd417c)

~~~json
{
  "source": "00bd417c",
  "target": "01126af0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126af0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4184`](#insn-00bd4184)

~~~json
{
  "source": "00bd4184",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd418c`](#insn-00bd418c)

~~~json
{
  "source": "00bd418c",
  "target": "01126ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd419c`](#insn-00bd419c)

~~~json
{
  "source": "00bd419c",
  "target": "01126ae8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ae8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41a4`](#insn-00bd41a4)

~~~json
{
  "source": "00bd41a4",
  "target": "01126b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41a8`](#insn-00bd41a8)

~~~json
{
  "source": "00bd41a8",
  "target": "00bd41ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd41b0`](#insn-00bd41b0)

~~~json
{
  "source": "00bd41b0",
  "target": "01126b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b10",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41b4`](#insn-00bd41b4)

~~~json
{
  "source": "00bd41b4",
  "target": "00bd41cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd41c8`](#insn-00bd41c8)

~~~json
{
  "source": "00bd41c8",
  "target": "01126b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b10",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41d0`](#insn-00bd41d0)

~~~json
{
  "source": "00bd41d0",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd41d8`](#insn-00bd41d8)

~~~json
{
  "source": "00bd41d8",
  "target": "01126b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41e8`](#insn-00bd41e8)

~~~json
{
  "source": "00bd41e8",
  "target": "01126b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41f0`](#insn-00bd41f0)

~~~json
{
  "source": "00bd41f0",
  "target": "01126b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd41f4`](#insn-00bd41f4)

~~~json
{
  "source": "00bd41f4",
  "target": "00bd4238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd41fc`](#insn-00bd41fc)

~~~json
{
  "source": "00bd41fc",
  "target": "01126b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4200`](#insn-00bd4200)

~~~json
{
  "source": "00bd4200",
  "target": "00bd4218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4214`](#insn-00bd4214)

~~~json
{
  "source": "00bd4214",
  "target": "01126b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b30",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd421c`](#insn-00bd421c)

~~~json
{
  "source": "00bd421c",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4224`](#insn-00bd4224)

~~~json
{
  "source": "00bd4224",
  "target": "01126b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4234`](#insn-00bd4234)

~~~json
{
  "source": "00bd4234",
  "target": "01126b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd423c`](#insn-00bd423c)

~~~json
{
  "source": "00bd423c",
  "target": "01126aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126aa8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4240`](#insn-00bd4240)

~~~json
{
  "source": "00bd4240",
  "target": "00bd4284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4248`](#insn-00bd4248)

~~~json
{
  "source": "00bd4248",
  "target": "01126ab0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ab0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd424c`](#insn-00bd424c)

~~~json
{
  "source": "00bd424c",
  "target": "00bd4264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4260`](#insn-00bd4260)

~~~json
{
  "source": "00bd4260",
  "target": "01126ab0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ab0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4268`](#insn-00bd4268)

~~~json
{
  "source": "00bd4268",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4270`](#insn-00bd4270)

~~~json
{
  "source": "00bd4270",
  "target": "01126aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126aa8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4280`](#insn-00bd4280)

~~~json
{
  "source": "00bd4280",
  "target": "01126aa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126aa8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd4284`](#insn-00bd4284)

~~~json
{
  "source": "00bd4284",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4288`](#insn-00bd4288)

~~~json
{
  "source": "00bd4288",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
