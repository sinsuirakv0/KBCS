# 00c4fafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c4eb08`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0091.md#compare-1500e7031725aab889419ee893f3c739)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c4fafc",
  "name": "FUN_00c4fafc",
  "size": 172,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c8c2f8df4f38095624864b2d986871d44d6ac51ab40bfc923db3b3fd530a5d59",
  "source_text_sha256": "c8c2f8df4f38095624864b2d986871d44d6ac51ab40bfc923db3b3fd530a5d59",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c4fafc",
        "00c4fba7"
      ]
    ],
    "bytes_sha256": "3356da47c065d21158ae4e3596b1d3f0cc7ef1d0eb861615cd0738a4fa71c2d8",
    "instruction_count": 43,
    "instruction_bytes": 172,
    "body_bytes": 172,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3bd5c](../00c3b/00c3bd5c.md)

## 呼び出し先

- [00c59080](../00c59/00c59080.md)
- [00c590c0](../00c59/00c590c0.md)
- [00c5b0c0](../00c5b/00c5b0c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1007 bytes

~~~c

undefined8 * FUN_00c4fafc(long param_1,char *param_2)

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
  *puVar4 = &PTR_FUN_00c986e0;
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
<a id="insn-00c4fafc"></a> `00c4fafc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c4fb00"></a> `00c4fb00` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00c4fb04"></a> `00c4fb04` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4fb08"></a> `00c4fb08` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4fb0c"></a> `00c4fb0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00c4fb10"></a> `00c4fb10` | `15 98 49 f9` | ldr x21,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4fb14"></a> `00c4fb14` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00c4fb18"></a> `00c4fb18` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00c4fb1c"></a> `00c4fb1c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c4fb20"></a> `00c4fb20` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c4fb24"></a> `00c4fb24` | `28 01 00 54` | b.hi 0x00c4fb48 | `CONDITIONAL_JUMP`
<a id="insn-00c4fb28"></a> `00c4fb28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c4fb2c"></a> `00c4fb2c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c4fb30"></a> `00c4fb30` | `64 2d 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c4fb34"></a> `00c4fb34` | `80 03 00 b4` | cbz x0,0x00c4fba4 | `CONDITIONAL_JUMP`
<a id="insn-00c4fb38"></a> `00c4fb38` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c4fb3c"></a> `00c4fb3c` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c4fb40"></a> `00c4fb40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c4fb44"></a> `00c4fb44` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00c4fb48"></a> `00c4fb48` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c4fb4c"></a> `00c4fb4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c4fb50"></a> `00c4fb50` | `b4 02 08 8b` | add x20,x21,x8 | `FALL_THROUGH`
<a id="insn-00c4fb54"></a> `00c4fb54` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00c4fb58"></a> `00c4fb58` | `4a 25 00 94` | bl 0x00c59080 | `UNCONDITIONAL_CALL`
<a id="insn-00c4fb5c"></a> `00c4fb5c` | `49 02 00 b0` | adrp x9,0xc98000 | `FALL_THROUGH`
<a id="insn-00c4fb60"></a> `00c4fb60` | `29 81 1b 91` | add x9,x9,#0x6e0 | `FALL_THROUGH`
<a id="insn-00c4fb64"></a> `00c4fb64` | `0b a8 80 52` | mov w11,#0x540 | `FALL_THROUGH`
<a id="insn-00c4fb68"></a> `00c4fb68` | `89 0e 01 f8` | str x9,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00c4fb6c"></a> `00c4fb6c` | `89 92 40 78` | ldurh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c4fb70"></a> `00c4fb70` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00c4fb74"></a> `00c4fb74` | `0a 01 80 52` | mov w10,#0x8 | `FALL_THROUGH`
<a id="insn-00c4fb78"></a> `00c4fb78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c4fb7c"></a> `00c4fb7c` | `29 0d 14 12` | and w9,w9,#0xf000 | `FALL_THROUGH`
<a id="insn-00c4fb80"></a> `00c4fb80` | `8a 22 00 39` | strb w10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c4fb84"></a> `00c4fb84` | `29 01 0b 2a` | orr w9,w9,w11 | `FALL_THROUGH`
<a id="insn-00c4fb88"></a> `00c4fb88` | `93 22 01 a9` | stp x19,x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00c4fb8c"></a> `00c4fb8c` | `89 92 00 78` | sturh w9,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00c4fb90"></a> `00c4fb90` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c4fb94"></a> `00c4fb94` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c4fb98"></a> `00c4fb98` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00c4fb9c"></a> `00c4fb9c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c4fba0"></a> `00c4fba0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c4fba4"></a> `00c4fba4` | `47 25 00 94` | bl 0x00c590c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c4fafc`](#insn-00c4fafc) 範囲 `[['00c4fafc', '00c4fb27']]`
  - `CONDITIONAL_JUMP` [`00c4fb24`](#insn-00c4fb24) → [`00c4fb48`](#insn-00c4fb48)
  - `FALL_THROUGH` [`00c4fb24`](#insn-00c4fb24) → [`00c4fb28`](#insn-00c4fb28)
- ブロック [`00c4fb28`](#insn-00c4fb28) 範囲 `[['00c4fb28', '00c4fb37']]`
  - `CONDITIONAL_JUMP` [`00c4fb34`](#insn-00c4fb34) → [`00c4fba4`](#insn-00c4fba4)
  - `FALL_THROUGH` [`00c4fb34`](#insn-00c4fb34) → [`00c4fb38`](#insn-00c4fb38)
- ブロック [`00c4fb38`](#insn-00c4fb38) 範囲 `[['00c4fb38', '00c4fb47']]`
  - `FALL_THROUGH` [`00c4fb44`](#insn-00c4fb44) → [`00c4fb48`](#insn-00c4fb48)
- ブロック [`00c4fb48`](#insn-00c4fb48) 範囲 `[['00c4fb48', '00c4fba3']]`
- ブロック [`00c4fba4`](#insn-00c4fba4) 範囲 `[['00c4fba4', '00c4fba7']]`

## 命令位置別の参照

- [`00c4fb00`](#insn-00c4fb00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb04`](#insn-00c4fb04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb08`](#insn-00c4fb08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb24`](#insn-00c4fb24) → [`00c4fb48`](#insn-00c4fb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb30`](#insn-00c4fb30) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb34`](#insn-00c4fb34) → [`00c4fba4`](#insn-00c4fba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb58`](#insn-00c4fb58) → [`00c59080`](../00c59/00c59080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59080` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb68`](#insn-00c4fb68) → `00c986e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c4fb90`](#insn-00c4fb90) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb94`](#insn-00c4fb94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fb98`](#insn-00c4fb98) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c4fba4`](#insn-00c4fba4) → [`00c590c0`](../00c59/00c590c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c4fb00`](#insn-00c4fb00)

~~~json
{
  "source": "00c4fb00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb04`](#insn-00c4fb04)

~~~json
{
  "source": "00c4fb04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb08`](#insn-00c4fb08)

~~~json
{
  "source": "00c4fb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb24`](#insn-00c4fb24)

~~~json
{
  "source": "00c4fb24",
  "target": "00c4fb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb30`](#insn-00c4fb30)

~~~json
{
  "source": "00c4fb30",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4fb34`](#insn-00c4fb34)

~~~json
{
  "source": "00c4fb34",
  "target": "00c4fba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb58`](#insn-00c4fb58)

~~~json
{
  "source": "00c4fb58",
  "target": "00c59080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c4fb68`](#insn-00c4fb68)

~~~json
{
  "source": "00c4fb68",
  "target": "00c986e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c986e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c4fb90`](#insn-00c4fb90)

~~~json
{
  "source": "00c4fb90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb94`](#insn-00c4fb94)

~~~json
{
  "source": "00c4fb94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fb98`](#insn-00c4fb98)

~~~json
{
  "source": "00c4fb98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c4fba4`](#insn-00c4fba4)

~~~json
{
  "source": "00c4fba4",
  "target": "00c590c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
