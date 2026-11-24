# 00bd1bfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd1bb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1bb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-a3affa9e1ce54f057b222e6f1c0ce54c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4e644`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e644.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-af61bd2ffa83b2283789eac0a2d8d210)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1bfc",
  "name": "FUN_00bd1bfc",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e30d0a6fbf37b792bceb6eab9a0fe519d1993965767d97ebb05de7435322567",
  "source_text_sha256": "0e30d0a6fbf37b792bceb6eab9a0fe519d1993965767d97ebb05de7435322567",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1bfc",
        "00bd1ca7"
      ]
    ],
    "bytes_sha256": "57c419737798bd46f6fb4d0f0f26a71e98eb81332a2e27c16ece8971019ff47a",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbde5c](../00bbd/00bbde5c.md)

## 呼び出し先

- [00bdb190](../00bdb/00bdb190.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1608 bytes

~~~c

undefined8 * FUN_00bd1bfc(long param_1,char *param_2)

{
  undefined8 *puVar1;
  size_t sVar2;
  long lVar3;
  undefined8 *puVar4;
  void *pvVar5;
  
  pvVar5 = *(void **)(param_1 + 0x1330);
  lVar3 = *(long *)((long)pvVar5 + 8);
  puVar1 = pvVar5;
  if (lVar3 - 0xfd0U < 0xfffffffffffff010) {
    puVar1 = malloc(0x1000);
    if (puVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      _ZSt9terminatev();
    }
    lVar3 = 0;
    *puVar1 = pvVar5;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
  *(long *)((long)puVar1 + 8) = lVar3 + 0x20;
  sVar2 = strlen(param_2);
  puVar4 = (undefined8 *)((long)puVar1 + lVar3 + 0x10);
  *puVar4 = &PTR_FUN_00c17898;
                    /* try { // try from 00bd1c78 to 00cd1de7 has its CatchHandler @ 00bd1c78
                       catch() { ... } // from try @ 00bd1c78 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd1ea8 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2140 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2308 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2760 with catch @ 00bd1c78
                       catch() { ... } // from try @ 00bd2858 with catch @ 00bd1c78 */
  *(undefined1 *)((long)puVar1 + lVar3 + 0x18) = 8;
  *(char **)((long)puVar1 + lVar3 + 0x20) = param_2;
  *(size_t *)((long)puVar1 + lVar3 + 0x28) = sVar2;
  *(ushort *)((long)puVar1 + lVar3 + 0x19) =
       *(ushort *)((long)puVar1 + lVar3 + 0x19) & 0xf000 | 0x540;
  return puVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1bfc"></a> `00bd1bfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd1c00"></a> `00bd1c00` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd1c04"></a> `00bd1c04` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1c08"></a> `00bd1c08` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1c0c"></a> `00bd1c0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd1c10"></a> `00bd1c10` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd1c14"></a> `00bd1c14` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd1c18"></a> `00bd1c18` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1c1c"></a> `00bd1c1c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bd1c20"></a> `00bd1c20` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bd1c24"></a> `00bd1c24` | `28 01 00 54` | b.hi 0x00bd1c48 | `CONDITIONAL_JUMP`
<a id="insn-00bd1c28"></a> `00bd1c28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd1c2c"></a> `00bd1c2c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bd1c30"></a> `00bd1c30` | `68 2d 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1c34"></a> `00bd1c34` | `80 03 00 b4` | cbz x0,0x00bd1ca4 | `CONDITIONAL_JUMP`
<a id="insn-00bd1c38"></a> `00bd1c38` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bd1c3c"></a> `00bd1c3c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bd1c40"></a> `00bd1c40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd1c44"></a> `00bd1c44` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd1c48"></a> `00bd1c48` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bd1c4c"></a> `00bd1c4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd1c50"></a> `00bd1c50` | `b4 02 08 8b` | add x20,x21,x8 | `FALL_THROUGH`
<a id="insn-00bd1c54"></a> `00bd1c54` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1c58"></a> `00bd1c58` | `4e 25 00 94` | bl 0x00bdb190 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1c5c"></a> `00bd1c5c` | `29 02 00 d0` | adrp x9,0xc17000 | `FALL_THROUGH`
<a id="insn-00bd1c60"></a> `00bd1c60` | `29 61 22 91` | add x9,x9,#0x898 | `FALL_THROUGH`
<a id="insn-00bd1c64"></a> `00bd1c64` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00bd1c68"></a> `00bd1c68` | `89 0e 01 f8` | str x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd1c6c"></a> `00bd1c6c` | `89 92 40 78` | ldurh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd1c70"></a> `00bd1c70` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd1c74"></a> `00bd1c74` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00bd1c78"></a> `00bd1c78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd1c7c"></a> `00bd1c7c` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00bd1c80"></a> `00bd1c80` | `8a 22 00 39` | strb w10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1c84"></a> `00bd1c84` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00bd1c88"></a> `00bd1c88` | `93 22 01 a9` | stp x19,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1c8c"></a> `00bd1c8c` | `89 92 00 78` | sturh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd1c90"></a> `00bd1c90` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1c94"></a> `00bd1c94` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1c98"></a> `00bd1c98` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd1c9c"></a> `00bd1c9c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd1ca0"></a> `00bd1ca0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd1ca4"></a> `00bd1ca4` | `4b 25 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1bfc`](#insn-00bd1bfc) 範囲 `[['00bd1bfc', '00bd1c27']]`
  - `CONDITIONAL_JUMP` [`00bd1c24`](#insn-00bd1c24) → [`00bd1c48`](#insn-00bd1c48)
  - `FALL_THROUGH` [`00bd1c24`](#insn-00bd1c24) → [`00bd1c28`](#insn-00bd1c28)
- ブロック [`00bd1c28`](#insn-00bd1c28) 範囲 `[['00bd1c28', '00bd1c37']]`
  - `CONDITIONAL_JUMP` [`00bd1c34`](#insn-00bd1c34) → [`00bd1ca4`](#insn-00bd1ca4)
  - `FALL_THROUGH` [`00bd1c34`](#insn-00bd1c34) → [`00bd1c38`](#insn-00bd1c38)
- ブロック [`00bd1c38`](#insn-00bd1c38) 範囲 `[['00bd1c38', '00bd1c47']]`
  - `FALL_THROUGH` [`00bd1c44`](#insn-00bd1c44) → [`00bd1c48`](#insn-00bd1c48)
- ブロック [`00bd1c48`](#insn-00bd1c48) 範囲 `[['00bd1c48', '00bd1c77']]`
  - `FALL_THROUGH` [`00bd1c74`](#insn-00bd1c74) → [`00bd1c78`](#insn-00bd1c78)
- ブロック [`00bd1c78`](#insn-00bd1c78) 範囲 `[['00bd1c78', '00bd1ca3']]`
- ブロック [`00bd1ca4`](#insn-00bd1ca4) 範囲 `[['00bd1ca4', '00bd1ca7']]`

## 命令位置別の参照

- [`00bd1c00`](#insn-00bd1c00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c04`](#insn-00bd1c04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c08`](#insn-00bd1c08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c24`](#insn-00bd1c24) → [`00bd1c48`](#insn-00bd1c48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c30`](#insn-00bd1c30) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c34`](#insn-00bd1c34) → [`00bd1ca4`](#insn-00bd1ca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c58`](#insn-00bd1c58) → [`00bdb190`](../00bdb/00bdb190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb190` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c68`](#insn-00bd1c68) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bd1c90`](#insn-00bd1c90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c94`](#insn-00bd1c94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1c98`](#insn-00bd1c98) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ca4`](#insn-00bd1ca4) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1c00`](#insn-00bd1c00)

~~~json
{
  "source": "00bd1c00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c04`](#insn-00bd1c04)

~~~json
{
  "source": "00bd1c04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c08`](#insn-00bd1c08)

~~~json
{
  "source": "00bd1c08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c24`](#insn-00bd1c24)

~~~json
{
  "source": "00bd1c24",
  "target": "00bd1c48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c30`](#insn-00bd1c30)

~~~json
{
  "source": "00bd1c30",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1c34`](#insn-00bd1c34)

~~~json
{
  "source": "00bd1c34",
  "target": "00bd1ca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c58`](#insn-00bd1c58)

~~~json
{
  "source": "00bd1c58",
  "target": "00bdb190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1c68`](#insn-00bd1c68)

~~~json
{
  "source": "00bd1c68",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd1c90`](#insn-00bd1c90)

~~~json
{
  "source": "00bd1c90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c94`](#insn-00bd1c94)

~~~json
{
  "source": "00bd1c94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1c98`](#insn-00bd1c98)

~~~json
{
  "source": "00bd1c98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ca4`](#insn-00bd1ca4)

~~~json
{
  "source": "00bd1ca4",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
