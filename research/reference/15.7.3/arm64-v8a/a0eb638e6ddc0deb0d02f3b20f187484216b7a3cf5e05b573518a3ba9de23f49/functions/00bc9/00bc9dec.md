# 00bc9dec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bc9d24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc9/00bc9d24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-16966cbd2bc8066e9a711a59722d9af4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bc9e30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-066100ce168db2cabbeebfffe86a50d6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc9dec",
  "name": "FUN_00bc9dec",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c2d9e6aca23499d66983878e4cac1166b336c985aef44d8e368d89c48dec5a07",
  "source_text_sha256": "c2d9e6aca23499d66983878e4cac1166b336c985aef44d8e368d89c48dec5a07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc9dec",
        "00bc9e8b"
      ]
    ],
    "bytes_sha256": "1079a971d0aaec4c0698b15504ef9c7198ec07a9512e406b74fa13c3cef7362b",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc489c](../00bc4/00bc489c.md)

## 呼び出し先

- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 909 bytes

~~~c

void FUN_00bc9dec(long param_1,undefined8 *param_2)

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
  *(long *)((long)puVar1 + 8) = lVar2 + 0x20;
  *(undefined ***)((long)puVar1 + lVar2 + 0x10) = &PTR_FUN_00c188d8;
  *(undefined1 *)((long)puVar1 + lVar2 + 0x18) = 0x4b;
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
<a id="insn-00bc9dec"></a> `00bc9dec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc9df0"></a> `00bc9df0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bc9df4"></a> `00bc9df4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9df8"></a> `00bc9df8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9dfc"></a> `00bc9dfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bc9e00"></a> `00bc9e00` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc9e04"></a> `00bc9e04` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bc9e08"></a> `00bc9e08` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9e0c"></a> `00bc9e0c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bc9e10"></a> `00bc9e10` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc9e14"></a> `00bc9e14` | `28 01 00 54` | b.hi 0x00bc9e38 | `CONDITIONAL_JUMP`
<a id="insn-00bc9e18"></a> `00bc9e18` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc9e1c"></a> `00bc9e1c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc9e20"></a> `00bc9e20` | `d8 4c 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9e24"></a> `00bc9e24` | `20 03 00 b4` | cbz x0,0x00bc9e88 | `CONDITIONAL_JUMP`
<a id="insn-00bc9e28"></a> `00bc9e28` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bc9e2c"></a> `00bc9e2c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc9e30"></a> `00bc9e30` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc9e34"></a> `00bc9e34` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc9e38"></a> `00bc9e38` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bc9e3c"></a> `00bc9e3c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bc9e40"></a> `00bc9e40` | `68 02 00 f0` | adrp x8,0xc18000 | `FALL_THROUGH`
<a id="insn-00bc9e44"></a> `00bc9e44` | `08 61 23 91` | add x8,x8,#0x8d8 | `FALL_THROUGH`
<a id="insn-00bc9e48"></a> `00bc9e48` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9e4c"></a> `00bc9e4c` | `69 09 80 52` | mov w9,#0x4b | `FALL_THROUGH`
<a id="insn-00bc9e50"></a> `00bc9e50` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc9e54"></a> `00bc9e54` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc9e58"></a> `00bc9e58` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bc9e5c"></a> `00bc9e5c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9e60"></a> `00bc9e60` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bc9e64"></a> `00bc9e64` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc9e68"></a> `00bc9e68` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bc9e6c"></a> `00bc9e6c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc9e70"></a> `00bc9e70` | `09 08 00 f9` | str x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9e74"></a> `00bc9e74` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc9e78"></a> `00bc9e78` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9e7c"></a> `00bc9e7c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bc9e80"></a> `00bc9e80` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc9e84"></a> `00bc9e84` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc9e88"></a> `00bc9e88` | `be 44 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc9dec`](#insn-00bc9dec) 範囲 `[['00bc9dec', '00bc9e17']]`
  - `CONDITIONAL_JUMP` [`00bc9e14`](#insn-00bc9e14) → [`00bc9e38`](#insn-00bc9e38)
  - `FALL_THROUGH` [`00bc9e14`](#insn-00bc9e14) → [`00bc9e18`](#insn-00bc9e18)
- ブロック [`00bc9e18`](#insn-00bc9e18) 範囲 `[['00bc9e18', '00bc9e27']]`
  - `CONDITIONAL_JUMP` [`00bc9e24`](#insn-00bc9e24) → [`00bc9e88`](#insn-00bc9e88)
  - `FALL_THROUGH` [`00bc9e24`](#insn-00bc9e24) → [`00bc9e28`](#insn-00bc9e28)
- ブロック [`00bc9e28`](#insn-00bc9e28) 範囲 `[['00bc9e28', '00bc9e37']]`
  - `FALL_THROUGH` [`00bc9e34`](#insn-00bc9e34) → [`00bc9e38`](#insn-00bc9e38)
- ブロック [`00bc9e38`](#insn-00bc9e38) 範囲 `[['00bc9e38', '00bc9e87']]`
- ブロック [`00bc9e88`](#insn-00bc9e88) 範囲 `[['00bc9e88', '00bc9e8b']]`

## 命令位置別の参照

- [`00bc9df0`](#insn-00bc9df0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9df4`](#insn-00bc9df4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9df8`](#insn-00bc9df8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e14`](#insn-00bc9e14) → [`00bc9e38`](#insn-00bc9e38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e20`](#insn-00bc9e20) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e24`](#insn-00bc9e24) → [`00bc9e88`](#insn-00bc9e88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e50`](#insn-00bc9e50) → `00c188d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc9e74`](#insn-00bc9e74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e78`](#insn-00bc9e78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e7c`](#insn-00bc9e7c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9e88`](#insn-00bc9e88) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc9df0`](#insn-00bc9df0)

~~~json
{
  "source": "00bc9df0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9df4`](#insn-00bc9df4)

~~~json
{
  "source": "00bc9df4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9df8`](#insn-00bc9df8)

~~~json
{
  "source": "00bc9df8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9e14`](#insn-00bc9e14)

~~~json
{
  "source": "00bc9e14",
  "target": "00bc9e38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9e20`](#insn-00bc9e20)

~~~json
{
  "source": "00bc9e20",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9e24`](#insn-00bc9e24)

~~~json
{
  "source": "00bc9e24",
  "target": "00bc9e88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9e50`](#insn-00bc9e50)

~~~json
{
  "source": "00bc9e50",
  "target": "00c188d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c188d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc9e74`](#insn-00bc9e74)

~~~json
{
  "source": "00bc9e74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9e78`](#insn-00bc9e78)

~~~json
{
  "source": "00bc9e78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9e7c`](#insn-00bc9e7c)

~~~json
{
  "source": "00bc9e7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9e88`](#insn-00bc9e88)

~~~json
{
  "source": "00bc9e88",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
