# 00af5bec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af5ba8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af5/00af5ba8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-61b032db048dddbd529ff243c48b53e3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b55970`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b55/00b55970.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-db266d613b66f669afe32c5a06d398bd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af5bec",
  "name": "_ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3dd07f7e3b42345148b85c96aaf5a2ef0a9a42da94f25e5a6a3d29d2b0792d8",
  "source_text_sha256": "a3dd07f7e3b42345148b85c96aaf5a2ef0a9a42da94f25e5a6a3d29d2b0792d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af5bec",
        "00af5c6f"
      ]
    ],
    "bytes_sha256": "604ebf1a681497884700bddb484b69262a7e465e366b761ba96badfa89d21141",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00bde5f0](../00bde/00bde5f0.md)

## 呼び出し先

- [00bde7e0](../00bde/00bde7e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1717 bytes

~~~c

void _ZN8firebase4util20JniByteArrayToVectorEP7_JNIEnvP8_jobject
               (undefined8 *param_1,long *param_2,undefined8 param_3)

{
  int iVar1;
  
                    /* try { // try from 00af5bf4 to 00bf5bfb has its CatchHandler @ 00affcd0 */
  *param_1 = 0;
  param_1[1] = 0;
                    /* try { // try from 00af5c00 to 00bf5c07 has its CatchHandler @ 00affcb8 */
  param_1[2] = 0;
                    /* try { // try from 00af5c0c to 00bf5c13 has its CatchHandler @ 00affcac */
                    /* try { // try from 00af5c18 to 00bf5c1f has its CatchHandler @ 00affc94 */
  iVar1 = (**(code **)(*param_2 + 0x558))();
  if (iVar1 != 0) {
                    /* try { // try from 00af5c24 to 00bf5c2b has its CatchHandler @ 00affc88 */
    _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE8__appendEm(param_1,(long)iVar1);
                    /* try { // try from 00af5c30 to 00bf5c37 has its CatchHandler @ 00affc70 */
                    /* try { // try from 00af5c3c to 00bf5c43 has its CatchHandler @ 00affc64 */
                    /* try { // try from 00af5c48 to 00bf5c4f has its CatchHandler @ 00affc4c */
    (**(code **)(*param_2 + 0x640))(param_2,param_3,0,iVar1,*param_1);
  }
                    /* try { // try from 00af5c54 to 00bf5c5b has its CatchHandler @ 00affc40 */
                    /* try { // try from 00af5c60 to 00bf5c67 has its CatchHandler @ 00affc28 */
                    /* WARNING: Could not recover jumptable at 0x00af5c6c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
                    /* try { // try from 00af5c6c to 00bf5c73 has its CatchHandler @ 00affc1c */
  (**(code **)(*param_2 + 0xb8))(param_2,param_3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af5bec"></a> `00af5bec` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af5bf0"></a> `00af5bf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5bf4"></a> `00af5bf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5bf8"></a> `00af5bf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00af5bfc"></a> `00af5bfc` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00af5c00"></a> `00af5c00` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00af5c04"></a> `00af5c04` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00af5c08"></a> `00af5c08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00af5c0c"></a> `00af5c0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af5c10"></a> `00af5c10` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00af5c14"></a> `00af5c14` | `08 ad 42 f9` | ldr x8,[x8, #0x558] | `FALL_THROUGH`
<a id="insn-00af5c18"></a> `00af5c18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af5c1c"></a> `00af5c1c` | `a0 01 00 34` | cbz w0,0x00af5c50 | `CONDITIONAL_JUMP`
<a id="insn-00af5c20"></a> `00af5c20` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00af5c24"></a> `00af5c24` | `c1 7e 40 93` | sxtw x1,w22 | `FALL_THROUGH`
<a id="insn-00af5c28"></a> `00af5c28` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af5c2c"></a> `00af5c2c` | `ed a2 03 94` | bl 0x00bde7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af5c30"></a> `00af5c30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af5c34"></a> `00af5c34` | `a4 02 40 f9` | ldr x4,[x21] | `FALL_THROUGH`
<a id="insn-00af5c38"></a> `00af5c38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5c3c"></a> `00af5c3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00af5c40"></a> `00af5c40` | `08 21 43 f9` | ldr x8,[x8, #0x640] | `FALL_THROUGH`
<a id="insn-00af5c44"></a> `00af5c44` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00af5c48"></a> `00af5c48` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-00af5c4c"></a> `00af5c4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af5c50"></a> `00af5c50` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af5c54"></a> `00af5c54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af5c58"></a> `00af5c58` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00af5c5c"></a> `00af5c5c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af5c60"></a> `00af5c60` | `02 5d 40 f9` | ldr x2,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00af5c64"></a> `00af5c64` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af5c68"></a> `00af5c68` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af5c6c"></a> `00af5c6c` | `40 00 1f d6` | br x2 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00af5bec`](#insn-00af5bec) 範囲 `[['00af5bec', '00af5bf3']]`
  - `FALL_THROUGH` [`00af5bf0`](#insn-00af5bf0) → [`00af5bf4`](#insn-00af5bf4)
- ブロック [`00af5bf4`](#insn-00af5bf4) 範囲 `[['00af5bf4', '00af5bff']]`
  - `FALL_THROUGH` [`00af5bfc`](#insn-00af5bfc) → [`00af5c00`](#insn-00af5c00)
- ブロック [`00af5c00`](#insn-00af5c00) 範囲 `[['00af5c00', '00af5c0b']]`
  - `FALL_THROUGH` [`00af5c08`](#insn-00af5c08) → [`00af5c0c`](#insn-00af5c0c)
- ブロック [`00af5c0c`](#insn-00af5c0c) 範囲 `[['00af5c0c', '00af5c17']]`
  - `FALL_THROUGH` [`00af5c14`](#insn-00af5c14) → [`00af5c18`](#insn-00af5c18)
- ブロック [`00af5c18`](#insn-00af5c18) 範囲 `[['00af5c18', '00af5c1f']]`
  - `CONDITIONAL_JUMP` [`00af5c1c`](#insn-00af5c1c) → [`00af5c50`](#insn-00af5c50)
  - `FALL_THROUGH` [`00af5c1c`](#insn-00af5c1c) → [`00af5c20`](#insn-00af5c20)
- ブロック [`00af5c20`](#insn-00af5c20) 範囲 `[['00af5c20', '00af5c23']]`
  - `FALL_THROUGH` [`00af5c20`](#insn-00af5c20) → [`00af5c24`](#insn-00af5c24)
- ブロック [`00af5c24`](#insn-00af5c24) 範囲 `[['00af5c24', '00af5c2f']]`
  - `FALL_THROUGH` [`00af5c2c`](#insn-00af5c2c) → [`00af5c30`](#insn-00af5c30)
- ブロック [`00af5c30`](#insn-00af5c30) 範囲 `[['00af5c30', '00af5c3b']]`
  - `FALL_THROUGH` [`00af5c38`](#insn-00af5c38) → [`00af5c3c`](#insn-00af5c3c)
- ブロック [`00af5c3c`](#insn-00af5c3c) 範囲 `[['00af5c3c', '00af5c47']]`
  - `FALL_THROUGH` [`00af5c44`](#insn-00af5c44) → [`00af5c48`](#insn-00af5c48)
- ブロック [`00af5c48`](#insn-00af5c48) 範囲 `[['00af5c48', '00af5c4f']]`
  - `FALL_THROUGH` [`00af5c4c`](#insn-00af5c4c) → [`00af5c50`](#insn-00af5c50)
- ブロック [`00af5c50`](#insn-00af5c50) 範囲 `[['00af5c50', '00af5c53']]`
  - `FALL_THROUGH` [`00af5c50`](#insn-00af5c50) → [`00af5c54`](#insn-00af5c54)
- ブロック [`00af5c54`](#insn-00af5c54) 範囲 `[['00af5c54', '00af5c5f']]`
  - `FALL_THROUGH` [`00af5c5c`](#insn-00af5c5c) → [`00af5c60`](#insn-00af5c60)
- ブロック [`00af5c60`](#insn-00af5c60) 範囲 `[['00af5c60', '00af5c6b']]`
  - `FALL_THROUGH` [`00af5c68`](#insn-00af5c68) → [`00af5c6c`](#insn-00af5c6c)
- ブロック [`00af5c6c`](#insn-00af5c6c) 範囲 `[['00af5c6c', '00af5c6f']]`

## 命令位置別の参照

- [`00af5bec`](#insn-00af5bec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5bf0`](#insn-00af5bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5bf4`](#insn-00af5bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c1c`](#insn-00af5c1c) → [`00af5c50`](#insn-00af5c50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c2c`](#insn-00af5c2c) → [`00bde7e0`](../00bde/00bde7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde7e0` · 推定シンボル `None` · 推定型 `None`
- [`00af5c5c`](#insn-00af5c5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af5c64`](#insn-00af5c64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af5bec`](#insn-00af5bec)

~~~json
{
  "source": "00af5bec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5bf0`](#insn-00af5bf0)

~~~json
{
  "source": "00af5bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5bf4`](#insn-00af5bf4)

~~~json
{
  "source": "00af5bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c1c`](#insn-00af5c1c)

~~~json
{
  "source": "00af5c1c",
  "target": "00af5c50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c2c`](#insn-00af5c2c)

~~~json
{
  "source": "00af5c2c",
  "target": "00bde7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af5c5c`](#insn-00af5c5c)

~~~json
{
  "source": "00af5c5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af5c64`](#insn-00af5c64)

~~~json
{
  "source": "00af5c64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
