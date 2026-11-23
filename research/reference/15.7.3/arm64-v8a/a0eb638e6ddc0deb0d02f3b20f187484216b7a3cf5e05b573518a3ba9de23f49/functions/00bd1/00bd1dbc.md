# 00bd1dbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bd1cf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd1/00bd1cf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-29d96a49562b3d88a92a92860bc1939f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bd1e00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-35a23f9b715bb71aa1fcc10caccb2c25)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1dbc",
  "name": "FUN_00bd1dbc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ceafba58556e4f706d6a21530029f589e8b52ba3f4b604312dc94541169f7183",
  "source_text_sha256": "ceafba58556e4f706d6a21530029f589e8b52ba3f4b604312dc94541169f7183",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1dbc",
        "00bd1e5b"
      ]
    ],
    "bytes_sha256": "5077eb3664b10144ab338430b9857ae99a1615eceff0fb8596e4f920c2b8129c",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbde18](../00bbd/00bbde18.md)

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1200 bytes

~~~c

void FUN_00bd1dbc(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  long lVar2;
  undefined8 uVar3;
  void *pvVar4;
  
  pvVar4 = *(void **)(param_1 + 0x1330);
  lVar2 = *(long *)((long)pvVar4 + 8);
  puVar1 = pvVar4;
  if (lVar2 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00bd1e58 to 00cd1e63 has its CatchHandler @ 00bd2904 */
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar4;
    puVar1[1] = 0;
                    /* try { // try from 00bd1e04 to 00cd1e13 has its CatchHandler @ 00bd291c */
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
                    /* try { // try from 00bd1e14 to 00cd1e23 has its CatchHandler @ 00bd290c */
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c19d68;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x1f;
  uVar3 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x540;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1dbc"></a> `00bd1dbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd1dc0"></a> `00bd1dc0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd1dc4"></a> `00bd1dc4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1dc8"></a> `00bd1dc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1dcc"></a> `00bd1dcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd1dd0"></a> `00bd1dd0` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd1dd4"></a> `00bd1dd4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd1dd8"></a> `00bd1dd8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1ddc"></a> `00bd1ddc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bd1de0"></a> `00bd1de0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bd1de4"></a> `00bd1de4` | `28 01 00 54` | b.hi 0x00bd1e08 | `CONDITIONAL_JUMP`
<a id="insn-00bd1de8"></a> `00bd1de8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd1dec"></a> `00bd1dec` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bd1df0"></a> `00bd1df0` | `e4 2c 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1df4"></a> `00bd1df4` | `20 03 00 b4` | cbz x0,0x00bd1e58 | `CONDITIONAL_JUMP`
<a id="insn-00bd1df8"></a> `00bd1df8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bd1dfc"></a> `00bd1dfc` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bd1e00"></a> `00bd1e00` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd1e04"></a> `00bd1e04` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd1e08"></a> `00bd1e08` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bd1e0c"></a> `00bd1e0c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bd1e10"></a> `00bd1e10` | `48 02 00 90` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bd1e14"></a> `00bd1e14` | `08 a1 35 91` | add x8,x8,#0xd68 | `FALL_THROUGH`
<a id="insn-00bd1e18"></a> `00bd1e18` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1e1c"></a> `00bd1e1c` | `e9 03 80 52` | mov w9,#0x1f | `FALL_THROUGH`
<a id="insn-00bd1e20"></a> `00bd1e20` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd1e24"></a> `00bd1e24` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd1e28"></a> `00bd1e28` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bd1e2c"></a> `00bd1e2c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1e30"></a> `00bd1e30` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bd1e34"></a> `00bd1e34` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bd1e38"></a> `00bd1e38` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bd1e3c"></a> `00bd1e3c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd1e40"></a> `00bd1e40` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1e44"></a> `00bd1e44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1e48"></a> `00bd1e48` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1e4c"></a> `00bd1e4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd1e50"></a> `00bd1e50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd1e54"></a> `00bd1e54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd1e58"></a> `00bd1e58` | `ca 24 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1dbc`](#insn-00bd1dbc) 範囲 `[['00bd1dbc', '00bd1de7']]`
  - `CONDITIONAL_JUMP` [`00bd1de4`](#insn-00bd1de4) → [`00bd1e08`](#insn-00bd1e08)
  - `FALL_THROUGH` [`00bd1de4`](#insn-00bd1de4) → [`00bd1de8`](#insn-00bd1de8)
- ブロック [`00bd1de8`](#insn-00bd1de8) 範囲 `[['00bd1de8', '00bd1df7']]`
  - `CONDITIONAL_JUMP` [`00bd1df4`](#insn-00bd1df4) → [`00bd1e58`](#insn-00bd1e58)
  - `FALL_THROUGH` [`00bd1df4`](#insn-00bd1df4) → [`00bd1df8`](#insn-00bd1df8)
- ブロック [`00bd1df8`](#insn-00bd1df8) 範囲 `[['00bd1df8', '00bd1e03']]`
  - `FALL_THROUGH` [`00bd1e00`](#insn-00bd1e00) → [`00bd1e04`](#insn-00bd1e04)
- ブロック [`00bd1e04`](#insn-00bd1e04) 範囲 `[['00bd1e04', '00bd1e07']]`
  - `FALL_THROUGH` [`00bd1e04`](#insn-00bd1e04) → [`00bd1e08`](#insn-00bd1e08)
- ブロック [`00bd1e08`](#insn-00bd1e08) 範囲 `[['00bd1e08', '00bd1e13']]`
  - `FALL_THROUGH` [`00bd1e10`](#insn-00bd1e10) → [`00bd1e14`](#insn-00bd1e14)
- ブロック [`00bd1e14`](#insn-00bd1e14) 範囲 `[['00bd1e14', '00bd1e57']]`
- ブロック [`00bd1e58`](#insn-00bd1e58) 範囲 `[['00bd1e58', '00bd1e5b']]`

## 命令位置別の参照

- [`00bd1dc0`](#insn-00bd1dc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1dc4`](#insn-00bd1dc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1dc8`](#insn-00bd1dc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1de4`](#insn-00bd1de4) → [`00bd1e08`](#insn-00bd1e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1df0`](#insn-00bd1df0) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bd1df4`](#insn-00bd1df4) → [`00bd1e58`](#insn-00bd1e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1e20`](#insn-00bd1e20) → `00c19d68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bd1e44`](#insn-00bd1e44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1e48`](#insn-00bd1e48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1e4c`](#insn-00bd1e4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1e58`](#insn-00bd1e58) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1dc0`](#insn-00bd1dc0)

~~~json
{
  "source": "00bd1dc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1dc4`](#insn-00bd1dc4)

~~~json
{
  "source": "00bd1dc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1dc8`](#insn-00bd1dc8)

~~~json
{
  "source": "00bd1dc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1de4`](#insn-00bd1de4)

~~~json
{
  "source": "00bd1de4",
  "target": "00bd1e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1df0`](#insn-00bd1df0)

~~~json
{
  "source": "00bd1df0",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1df4`](#insn-00bd1df4)

~~~json
{
  "source": "00bd1df4",
  "target": "00bd1e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1e20`](#insn-00bd1e20)

~~~json
{
  "source": "00bd1e20",
  "target": "00c19d68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19d68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd1e44`](#insn-00bd1e44)

~~~json
{
  "source": "00bd1e44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1e48`](#insn-00bd1e48)

~~~json
{
  "source": "00bd1e48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1e4c`](#insn-00bd1e4c)

~~~json
{
  "source": "00bd1e4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1e58`](#insn-00bd1e58)

~~~json
{
  "source": "00bd1e58",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
