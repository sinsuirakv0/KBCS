# 00a3eccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `009e1dd0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e1/009e1dd0.md) · 移動量 `+0x5cefc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0050.md#compare-fbc54dfd1bcdd519d50c6f2b1c6bdb07)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3eec4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3eec4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0060.md#compare-79fdb0690213d4b5a70462e031aaf7dd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3eccc",
  "name": "FUN_00a3eccc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c3a949852d9d09b5fb8101efa48d200fafe5bffbdaaeb1a8db622b1352048e9",
  "source_text_sha256": "9c3a949852d9d09b5fb8101efa48d200fafe5bffbdaaeb1a8db622b1352048e9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3eccc",
        "00a3ed53"
      ]
    ],
    "bytes_sha256": "2922d2e00170d53f7991c250ffa5286bda537fc1a62d258f7849635608c30853",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006917c0](../00691/006917c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 483 bytes

~~~c

void FUN_00a3eccc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[3] = 0;
  param_2[2] = param_2 + 3;
  param_2[1] = uVar1;
  param_2[4] = 0;
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *param_2 = &PTR_FUN_00c8b0a8;
  FUN_006917c0(param_2 + 2,uVar1,param_1 + 0x18);
  param_2[6] = 0;
  param_2[5] = param_2 + 6;
  param_2[7] = 0;
  FUN_006917c0(param_2 + 5,*(undefined8 *)(param_1 + 0x28),param_1 + 0x30);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3eccc"></a> `00a3eccc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00a3ecd0"></a> `00a3ecd0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ecd4"></a> `00a3ecd4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ecd8"></a> `00a3ecd8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3ecdc"></a> `00a3ecdc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3ece0"></a> `00a3ece0` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00a3ece4"></a> `00a3ece4` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00a3ece8"></a> `00a3ece8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00a3ecec"></a> `00a3ecec` | `df 8e 01 f8` | str xzr,[x22, #0x18]! | `FALL_THROUGH`
<a id="insn-00a3ecf0"></a> `00a3ecf0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00a3ecf4"></a> `00a3ecf4` | `76 0e 01 f8` | str x22,[x19, #0x10]! | `FALL_THROUGH`
<a id="insn-00a3ecf8"></a> `00a3ecf8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00a3ecfc"></a> `00a3ecfc` | `28 04 00 f9` | str x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00a3ed00"></a> `00a3ed00` | `68 12 00 b0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a3ed04"></a> `00a3ed04` | `08 a1 02 91` | add x8,x8,#0xa8 | `FALL_THROUGH`
<a id="insn-00a3ed08"></a> `00a3ed08` | `3f 10 00 f9` | str xzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ed0c"></a> `00a3ed0c` | `01 08 40 f9` | ldr x1,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ed10"></a> `00a3ed10` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00a3ed14"></a> `00a3ed14` | `02 60 00 91` | add x2,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00a3ed18"></a> `00a3ed18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3ed1c"></a> `00a3ed1c` | `a9 4a f1 97` | bl 0x006917c0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ed20"></a> `00a3ed20` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00a3ed24"></a> `00a3ed24` | `ff 0e 03 f8` | str xzr,[x23, #0x30]! | `FALL_THROUGH`
<a id="insn-00a3ed28"></a> `00a3ed28` | `97 8e 02 f8` | str x23,[x20, #0x28]! | `FALL_THROUGH`
<a id="insn-00a3ed2c"></a> `00a3ed2c` | `9f 0a 00 f9` | str xzr,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ed30"></a> `00a3ed30` | `a1 16 40 f9` | ldr x1,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00a3ed34"></a> `00a3ed34` | `a2 c2 00 91` | add x2,x21,#0x30 | `FALL_THROUGH`
<a id="insn-00a3ed38"></a> `00a3ed38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a3ed3c"></a> `00a3ed3c` | `a1 4a f1 97` | bl 0x006917c0 | `UNCONDITIONAL_CALL`
<a id="insn-00a3ed40"></a> `00a3ed40` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3ed44"></a> `00a3ed44` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ed48"></a> `00a3ed48` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3ed4c"></a> `00a3ed4c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00a3ed50"></a> `00a3ed50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3eccc`](#insn-00a3eccc) 範囲 `[['00a3eccc', '00a3ed53']]`

## 命令位置別の参照

- [`00a3eccc`](#insn-00a3eccc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ecd0`](#insn-00a3ecd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ecd4`](#insn-00a3ecd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ecd8`](#insn-00a3ecd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ed10`](#insn-00a3ed10) → `00c8b0a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3ed1c`](#insn-00a3ed1c) → [`006917c0`](../00691/006917c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006917c0` · 推定シンボル `None` · 推定型 `None`
- [`00a3ed3c`](#insn-00a3ed3c) → [`006917c0`](../00691/006917c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006917c0` · 推定シンボル `None` · 推定型 `None`
- [`00a3ed40`](#insn-00a3ed40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ed44`](#insn-00a3ed44) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ed48`](#insn-00a3ed48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ed4c`](#insn-00a3ed4c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3eccc`](#insn-00a3eccc)

~~~json
{
  "source": "00a3eccc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ecd0`](#insn-00a3ecd0)

~~~json
{
  "source": "00a3ecd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ecd4`](#insn-00a3ecd4)

~~~json
{
  "source": "00a3ecd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ecd8`](#insn-00a3ecd8)

~~~json
{
  "source": "00a3ecd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ed10`](#insn-00a3ed10)

~~~json
{
  "source": "00a3ed10",
  "target": "00c8b0a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b0a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3ed1c`](#insn-00a3ed1c)

~~~json
{
  "source": "00a3ed1c",
  "target": "006917c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ed3c`](#insn-00a3ed3c)

~~~json
{
  "source": "00a3ed3c",
  "target": "006917c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ed40`](#insn-00a3ed40)

~~~json
{
  "source": "00a3ed40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ed44`](#insn-00a3ed44)

~~~json
{
  "source": "00a3ed44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ed48`](#insn-00a3ed48)

~~~json
{
  "source": "00a3ed48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ed4c`](#insn-00a3ed4c)

~~~json
{
  "source": "00a3ed4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
