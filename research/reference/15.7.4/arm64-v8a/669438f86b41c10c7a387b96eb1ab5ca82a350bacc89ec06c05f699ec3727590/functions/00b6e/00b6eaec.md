# 00b6eaec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6eaa8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eaa8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-449d397cdefe0d936e4db91b22af46fb)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bddfec`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bddfec.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-9f7de7c36ed6f0b3b0347b1f9721a01d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6eaec",
  "name": "_ZNK8firebase4auth4User12display_nameEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e50e39f7eeafc07b476f1c07f16fb0bb3cd7e4aa490b4918c9af80fc356f3e81",
  "source_text_sha256": "e50e39f7eeafc07b476f1c07f16fb0bb3cd7e4aa490b4918c9af80fc356f3e81",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6eaec",
        "00b6eb8f"
      ]
    ],
    "bytes_sha256": "c2a12ec616213bbd209db5d2497572c5387d44a5d5a7790f7a1219a08bd5e53a",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde0e0](../00bde/00bde0e0.md)
- [00bde200](../00bde/00bde200.md)
- [00bde510](../00bde/00bde510.md)
- [00bde740](../00bde/00bde740.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 991 bytes

~~~c

void _ZNK8firebase4auth4User12display_nameEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
                    /* try { // try from 00b6eb70 to 00c6eb87 has its CatchHandler @ 00b7076c */
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002967d9);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_0047495c(uVar1,lVar4,DAT_010a1ac8);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00b6eb88 to 00c6ec3b has its CatchHandler @ 00b6e440 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6eaec"></a> `00b6eaec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6eaf0"></a> `00b6eaf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eaf4"></a> `00b6eaf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6eaf8"></a> `00b6eaf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6eafc"></a> `00b6eafc` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6eb00"></a> `00b6eb00` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6eb04"></a> `00b6eb04` | `c9 02 00 b4` | cbz x9,0x00b6eb5c | `CONDITIONAL_JUMP`
<a id="insn-00b6eb08"></a> `00b6eb08` | `35 01 41 f9` | ldr x21,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00b6eb0c"></a> `00b6eb0c` | `95 02 00 b4` | cbz x21,0x00b6eb5c | `CONDITIONAL_JUMP`
<a id="insn-00b6eb10"></a> `00b6eb10` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00b6eb14"></a> `00b6eb14` | `bb bd 01 94` | bl 0x00bde200 | `UNCONDITIONAL_CALL`
<a id="insn-00b6eb18"></a> `00b6eb18` | `88 29 00 f0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6eb1c"></a> `00b6eb1c` | `02 65 45 f9` | ldr x2,[x8, #0xac8] | `FALL_THROUGH`
<a id="insn-00b6eb20"></a> `00b6eb20` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6eb24"></a> `00b6eb24` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6eb28"></a> `00b6eb28` | `8d 17 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6eb2c"></a> `00b6eb2c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6eb30"></a> `00b6eb30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6eb34"></a> `00b6eb34` | `6b bd 01 94` | bl 0x00bde0e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6eb38"></a> `00b6eb38` | `15 02 00 b4` | cbz x21,0x00b6eb78 | `CONDITIONAL_JUMP`
<a id="insn-00b6eb3c"></a> `00b6eb3c` | `e0 01 00 37` | tbnz w0,#0x0,0x00b6eb78 | `CONDITIONAL_JUMP`
<a id="insn-00b6eb40"></a> `00b6eb40` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b6eb44"></a> `00b6eb44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6eb48"></a> `00b6eb48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6eb4c"></a> `00b6eb4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eb50"></a> `00b6eb50` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6eb54"></a> `00b6eb54` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6eb58"></a> `00b6eb58` | `6e be 01 14` | b 0x00bde510 | `CALL_TERMINATOR`
<a id="insn-00b6eb5c"></a> `00b6eb5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6eb60"></a> `00b6eb60` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6eb64"></a> `00b6eb64` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eb68"></a> `00b6eb68` | `41 b9 ff 90` | adrp x1,0x296000 | `FALL_THROUGH`
<a id="insn-00b6eb6c"></a> `00b6eb6c` | `21 64 1f 91` | add x1,x1,#0x7d9 | `FALL_THROUGH`
<a id="insn-00b6eb70"></a> `00b6eb70` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6eb74"></a> `00b6eb74` | `f3 be 01 14` | b 0x00bde740 | `CALL_TERMINATOR`
<a id="insn-00b6eb78"></a> `00b6eb78` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6eb7c"></a> `00b6eb7c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eb80"></a> `00b6eb80` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6eb84"></a> `00b6eb84` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6eb88"></a> `00b6eb88` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6eb8c"></a> `00b6eb8c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6eaec`](#insn-00b6eaec) 範囲 `[['00b6eaec', '00b6eb07']]`
  - `CONDITIONAL_JUMP` [`00b6eb04`](#insn-00b6eb04) → [`00b6eb5c`](#insn-00b6eb5c)
  - `FALL_THROUGH` [`00b6eb04`](#insn-00b6eb04) → [`00b6eb08`](#insn-00b6eb08)
- ブロック [`00b6eb08`](#insn-00b6eb08) 範囲 `[['00b6eb08', '00b6eb0f']]`
  - `CONDITIONAL_JUMP` [`00b6eb0c`](#insn-00b6eb0c) → [`00b6eb5c`](#insn-00b6eb5c)
  - `FALL_THROUGH` [`00b6eb0c`](#insn-00b6eb0c) → [`00b6eb10`](#insn-00b6eb10)
- ブロック [`00b6eb10`](#insn-00b6eb10) 範囲 `[['00b6eb10', '00b6eb3b']]`
  - `CONDITIONAL_JUMP` [`00b6eb38`](#insn-00b6eb38) → [`00b6eb78`](#insn-00b6eb78)
  - `FALL_THROUGH` [`00b6eb38`](#insn-00b6eb38) → [`00b6eb3c`](#insn-00b6eb3c)
- ブロック [`00b6eb3c`](#insn-00b6eb3c) 範囲 `[['00b6eb3c', '00b6eb3f']]`
  - `CONDITIONAL_JUMP` [`00b6eb3c`](#insn-00b6eb3c) → [`00b6eb78`](#insn-00b6eb78)
  - `FALL_THROUGH` [`00b6eb3c`](#insn-00b6eb3c) → [`00b6eb40`](#insn-00b6eb40)
- ブロック [`00b6eb40`](#insn-00b6eb40) 範囲 `[['00b6eb40', '00b6eb5b']]`
- ブロック [`00b6eb5c`](#insn-00b6eb5c) 範囲 `[['00b6eb5c', '00b6eb6f']]`
  - `FALL_THROUGH` [`00b6eb6c`](#insn-00b6eb6c) → [`00b6eb70`](#insn-00b6eb70)
- ブロック [`00b6eb70`](#insn-00b6eb70) 範囲 `[['00b6eb70', '00b6eb77']]`
- ブロック [`00b6eb78`](#insn-00b6eb78) 範囲 `[['00b6eb78', '00b6eb87']]`
  - `FALL_THROUGH` [`00b6eb84`](#insn-00b6eb84) → [`00b6eb88`](#insn-00b6eb88)
- ブロック [`00b6eb88`](#insn-00b6eb88) 範囲 `[['00b6eb88', '00b6eb8f']]`

## 命令位置別の参照

- [`00b6eaec`](#insn-00b6eaec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eaf0`](#insn-00b6eaf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eaf4`](#insn-00b6eaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb04`](#insn-00b6eb04) → [`00b6eb5c`](#insn-00b6eb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb0c`](#insn-00b6eb0c) → [`00b6eb5c`](#insn-00b6eb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb14`](#insn-00b6eb14) → [`00bde200`](../00bde/00bde200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde200` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb1c`](#insn-00b6eb1c) → `010a1ac8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6eb28`](#insn-00b6eb28) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb34`](#insn-00b6eb34) → [`00bde0e0`](../00bde/00bde0e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0e0` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb38`](#insn-00b6eb38) → [`00b6eb78`](#insn-00b6eb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb3c`](#insn-00b6eb3c) → [`00b6eb78`](#insn-00b6eb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb48`](#insn-00b6eb48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb4c`](#insn-00b6eb4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb58`](#insn-00b6eb58) → [`00bde510`](../00bde/00bde510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde510` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb60`](#insn-00b6eb60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb64`](#insn-00b6eb64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb6c`](#insn-00b6eb6c) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b6eb74`](#insn-00b6eb74) → [`00bde740`](../00bde/00bde740.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde740` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb80`](#insn-00b6eb80) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6eb84`](#insn-00b6eb84) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6eaec`](#insn-00b6eaec)

~~~json
{
  "source": "00b6eaec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eaf0`](#insn-00b6eaf0)

~~~json
{
  "source": "00b6eaf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eaf4`](#insn-00b6eaf4)

~~~json
{
  "source": "00b6eaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb04`](#insn-00b6eb04)

~~~json
{
  "source": "00b6eb04",
  "target": "00b6eb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb0c`](#insn-00b6eb0c)

~~~json
{
  "source": "00b6eb0c",
  "target": "00b6eb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb14`](#insn-00b6eb14)

~~~json
{
  "source": "00b6eb14",
  "target": "00bde200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6eb1c`](#insn-00b6eb1c)

~~~json
{
  "source": "00b6eb1c",
  "target": "010a1ac8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1ac8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6eb28`](#insn-00b6eb28)

~~~json
{
  "source": "00b6eb28",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6eb34`](#insn-00b6eb34)

~~~json
{
  "source": "00b6eb34",
  "target": "00bde0e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6eb38`](#insn-00b6eb38)

~~~json
{
  "source": "00b6eb38",
  "target": "00b6eb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb3c`](#insn-00b6eb3c)

~~~json
{
  "source": "00b6eb3c",
  "target": "00b6eb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb48`](#insn-00b6eb48)

~~~json
{
  "source": "00b6eb48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb4c`](#insn-00b6eb4c)

~~~json
{
  "source": "00b6eb4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb58`](#insn-00b6eb58)

~~~json
{
  "source": "00b6eb58",
  "target": "00bde510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6eb60`](#insn-00b6eb60)

~~~json
{
  "source": "00b6eb60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb64`](#insn-00b6eb64)

~~~json
{
  "source": "00b6eb64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb6c`](#insn-00b6eb6c)

~~~json
{
  "source": "00b6eb6c",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b6eb74`](#insn-00b6eb74)

~~~json
{
  "source": "00b6eb74",
  "target": "00bde740",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6eb80`](#insn-00b6eb80)

~~~json
{
  "source": "00b6eb80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6eb84`](#insn-00b6eb84)

~~~json
{
  "source": "00b6eb84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
