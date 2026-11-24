# 00bcb5dc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcb598`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcb/00bcb598.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-36eb09af9b418a4072a3ada756305b2b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c48024`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-60933f8eb3ed4d20ce6a7ca78b19f361)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcb5dc",
  "name": "FUN_00bcb5dc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e580dbf6de9ff6fa32c77570d8bda787bce99b43ba9178c1b8dc66c6796df6e",
  "source_text_sha256": "2e580dbf6de9ff6fa32c77570d8bda787bce99b43ba9178c1b8dc66c6796df6e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcb5dc",
        "00bcb67b"
      ]
    ],
    "bytes_sha256": "1387d010d3de02d6da87f766363af622e59e648511b98c3660d164f0bafd0db4",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bca9c4](../00bca/00bca9c4.md)

## 呼び出し先

- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 996 bytes

~~~c

void FUN_00bcb5dc(long param_1,undefined8 *param_2)

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
      _ZSt9terminatev();
    }
    lVar2 = 0;
    *puVar1 = pvVar4;
    puVar1[1] = 0;
    *(undefined8 **)(param_1 + 0x1330) = puVar1;
  }
                    /* catch() { ... } // from try @ 00bcb804 with catch @ 00bcb628 */
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c18848;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x27;
  uVar3 = *param_2;
  *(ushort *)((long)puVar1 + lVar2 + 0x19) =
       *(ushort *)((long)puVar1 + lVar2 + 0x19) & 0xf000 | 0x500;
  *(undefined8 *)((long)puVar1 + lVar2 + 0x20) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcb5dc"></a> `00bcb5dc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcb5e0"></a> `00bcb5e0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcb5e4"></a> `00bcb5e4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb5e8"></a> `00bcb5e8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb5ec"></a> `00bcb5ec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcb5f0"></a> `00bcb5f0` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcb5f4"></a> `00bcb5f4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcb5f8"></a> `00bcb5f8` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb5fc"></a> `00bcb5fc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bcb600"></a> `00bcb600` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bcb604"></a> `00bcb604` | `28 01 00 54` | b.hi 0x00bcb628 | `CONDITIONAL_JUMP`
<a id="insn-00bcb608"></a> `00bcb608` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcb60c"></a> `00bcb60c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bcb610"></a> `00bcb610` | `f0 46 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb614"></a> `00bcb614` | `20 03 00 b4` | cbz x0,0x00bcb678 | `CONDITIONAL_JUMP`
<a id="insn-00bcb618"></a> `00bcb618` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bcb61c"></a> `00bcb61c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bcb620"></a> `00bcb620` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcb624"></a> `00bcb624` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bcb628"></a> `00bcb628` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bcb62c"></a> `00bcb62c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bcb630"></a> `00bcb630` | `68 02 00 b0` | adrp x8,0xc18000 | `FALL_THROUGH`
<a id="insn-00bcb634"></a> `00bcb634` | `08 21 21 91` | add x8,x8,#0x848 | `FALL_THROUGH`
<a id="insn-00bcb638"></a> `00bcb638` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb63c"></a> `00bcb63c` | `e9 04 80 52` | mov w9,#0x27 | `FALL_THROUGH`
<a id="insn-00bcb640"></a> `00bcb640` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bcb644"></a> `00bcb644` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcb648"></a> `00bcb648` | `0a a0 80 52` | mov w10,#0x500 | `FALL_THROUGH`
<a id="insn-00bcb64c"></a> `00bcb64c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb650"></a> `00bcb650` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bcb654"></a> `00bcb654` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bcb658"></a> `00bcb658` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bcb65c"></a> `00bcb65c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bcb660"></a> `00bcb660` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb664"></a> `00bcb664` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb668"></a> `00bcb668` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb66c"></a> `00bcb66c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcb670"></a> `00bcb670` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcb674"></a> `00bcb674` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcb678"></a> `00bcb678` | `d6 3e 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcb5dc`](#insn-00bcb5dc) 範囲 `[['00bcb5dc', '00bcb607']]`
  - `CONDITIONAL_JUMP` [`00bcb604`](#insn-00bcb604) → [`00bcb628`](#insn-00bcb628)
  - `FALL_THROUGH` [`00bcb604`](#insn-00bcb604) → [`00bcb608`](#insn-00bcb608)
- ブロック [`00bcb608`](#insn-00bcb608) 範囲 `[['00bcb608', '00bcb617']]`
  - `CONDITIONAL_JUMP` [`00bcb614`](#insn-00bcb614) → [`00bcb678`](#insn-00bcb678)
  - `FALL_THROUGH` [`00bcb614`](#insn-00bcb614) → [`00bcb618`](#insn-00bcb618)
- ブロック [`00bcb618`](#insn-00bcb618) 範囲 `[['00bcb618', '00bcb627']]`
  - `FALL_THROUGH` [`00bcb624`](#insn-00bcb624) → [`00bcb628`](#insn-00bcb628)
- ブロック [`00bcb628`](#insn-00bcb628) 範囲 `[['00bcb628', '00bcb677']]`
- ブロック [`00bcb678`](#insn-00bcb678) 範囲 `[['00bcb678', '00bcb67b']]`

## 命令位置別の参照

- [`00bcb5e0`](#insn-00bcb5e0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb5e4`](#insn-00bcb5e4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb5e8`](#insn-00bcb5e8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb604`](#insn-00bcb604) → [`00bcb628`](#insn-00bcb628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb610`](#insn-00bcb610) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb614`](#insn-00bcb614) → [`00bcb678`](#insn-00bcb678) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb640`](#insn-00bcb640) → `00c18848`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bcb664`](#insn-00bcb664) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb668`](#insn-00bcb668) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb66c`](#insn-00bcb66c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb678`](#insn-00bcb678) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcb5e0`](#insn-00bcb5e0)

~~~json
{
  "source": "00bcb5e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb5e4`](#insn-00bcb5e4)

~~~json
{
  "source": "00bcb5e4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb5e8`](#insn-00bcb5e8)

~~~json
{
  "source": "00bcb5e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb604`](#insn-00bcb604)

~~~json
{
  "source": "00bcb604",
  "target": "00bcb628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb610`](#insn-00bcb610)

~~~json
{
  "source": "00bcb610",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb614`](#insn-00bcb614)

~~~json
{
  "source": "00bcb614",
  "target": "00bcb678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb640`](#insn-00bcb640)

~~~json
{
  "source": "00bcb640",
  "target": "00c18848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c18848",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcb664`](#insn-00bcb664)

~~~json
{
  "source": "00bcb664",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb668`](#insn-00bcb668)

~~~json
{
  "source": "00bcb668",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb66c`](#insn-00bcb66c)

~~~json
{
  "source": "00bcb66c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb678`](#insn-00bcb678)

~~~json
{
  "source": "00bcb678",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
