# 00b6ddfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b6dd60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-63e57e5da19504bb8db40a4ba7cca546)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b6edf0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6edf0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0033.md#compare-c120d63d7f8b0d8217f81f836f47df7a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6ddfc",
  "name": "_ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc57a5e42dc2f7608f2264d076c0519886baf94a98cc5f0202c48395eb4678cd",
  "source_text_sha256": "cc57a5e42dc2f7608f2264d076c0519886baf94a98cc5f0202c48395eb4678cd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6ddfc",
        "00b6de8b"
      ]
    ],
    "bytes_sha256": "4a6fdf8fc2b7a8eb29caf7d21fb5baa6b3f407890d2cd54bfcab86d0690ca1c8",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5b9a0](../00c5b/00c5b9a0.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5b940](../00c5b/00c5b940.md)
- [00c5bb60](../00c5b/00c5bb60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1086 bytes

~~~c

void _ZN11flatbuffers11SymbolTableINS_8FieldDefEED2Ev(long param_1)

{
  undefined8 *puVar1;
  undefined8 *__ptr;
  void *__ptr_00;
  
  __ptr = *(undefined8 **)(param_1 + 0x18);
  puVar1 = *(undefined8 **)(param_1 + 0x20);
  if (__ptr != puVar1) {
    do {
      __ptr_00 = (void *)*__ptr;
      if (__ptr_00 != (void *)0x0) {
        if ((*(byte *)((long)__ptr_00 + 0xc0) & 1) != 0) {
          _ZdlPv(*(void **)((long)__ptr_00 + 0xd0));
        }
        _ZN11flatbuffers10DefinitionD2Ev(__ptr_00);
        _ZdlPv(__ptr_00);
        puVar1 = *(undefined8 **)(param_1 + 0x20);
      }
      __ptr = __ptr + 1;
    } while (__ptr != puVar1);
    __ptr = *(undefined8 **)(param_1 + 0x18);
  }
  if (__ptr != (undefined8 *)0x0) {
    *(undefined8 **)(param_1 + 0x20) = __ptr;
    _ZdlPv(__ptr);
  }
  _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
            (param_1,*(undefined8 *)(param_1 + 8));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6ddfc"></a> `00b6ddfc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6de00"></a> `00b6de00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6de04"></a> `00b6de04` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6de08"></a> `00b6de08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6de0c"></a> `00b6de0c` | `14 a0 41 a9` | ldp x20,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00b6de10"></a> `00b6de10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6de14"></a> `00b6de14` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00b6de18"></a> `00b6de18` | `61 02 00 54` | b.ne 0x00b6de64 | `CONDITIONAL_JUMP`
<a id="insn-00b6de1c"></a> `00b6de1c` | `94 00 00 b4` | cbz x20,0x00b6de2c | `CONDITIONAL_JUMP`
<a id="insn-00b6de20"></a> `00b6de20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6de24"></a> `00b6de24` | `74 12 00 f9` | str x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6de28"></a> `00b6de28` | `56 a8 03 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b6de2c"></a> `00b6de2c` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6de30"></a> `00b6de30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6de34"></a> `00b6de34` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6de38"></a> `00b6de38` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6de3c"></a> `00b6de3c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6de40"></a> `00b6de40` | `48 b7 03 14` | b 0x00c5bb60 | `CALL_TERMINATOR`
<a id="insn-00b6de44"></a> `00b6de44` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6de48"></a> `00b6de48` | `be b6 03 94` | bl 0x00c5b940 | `UNCONDITIONAL_CALL`
<a id="insn-00b6de4c"></a> `00b6de4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b6de50"></a> `00b6de50` | `4c a8 03 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b6de54"></a> `00b6de54` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6de58"></a> `00b6de58` | `94 22 00 91` | add x20,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00b6de5c"></a> `00b6de5c` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00b6de60"></a> `00b6de60` | `00 01 00 54` | b.eq 0x00b6de80 | `CONDITIONAL_JUMP`
<a id="insn-00b6de64"></a> `00b6de64` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00b6de68"></a> `00b6de68` | `95 ff ff b4` | cbz x21,0x00b6de58 | `CONDITIONAL_JUMP`
<a id="insn-00b6de6c"></a> `00b6de6c` | `a8 02 43 39` | ldrb w8,[x21, #0xc0] | `FALL_THROUGH`
<a id="insn-00b6de70"></a> `00b6de70` | `a8 fe 07 36` | tbz w8,#0x0,0x00b6de44 | `CONDITIONAL_JUMP`
<a id="insn-00b6de74"></a> `00b6de74` | `a0 6a 40 f9` | ldr x0,[x21, #0xd0] | `FALL_THROUGH`
<a id="insn-00b6de78"></a> `00b6de78` | `42 a8 03 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b6de7c"></a> `00b6de7c` | `f2 ff ff 17` | b 0x00b6de44 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6de80"></a> `00b6de80` | `74 0e 40 f9` | ldr x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6de84"></a> `00b6de84` | `f4 fc ff b5` | cbnz x20,0x00b6de20 | `CONDITIONAL_JUMP`
<a id="insn-00b6de88"></a> `00b6de88` | `e9 ff ff 17` | b 0x00b6de2c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b6ddfc`](#insn-00b6ddfc) 範囲 `[['00b6ddfc', '00b6de1b']]`
  - `CONDITIONAL_JUMP` [`00b6de18`](#insn-00b6de18) → [`00b6de64`](#insn-00b6de64)
  - `FALL_THROUGH` [`00b6de18`](#insn-00b6de18) → [`00b6de1c`](#insn-00b6de1c)
- ブロック [`00b6de1c`](#insn-00b6de1c) 範囲 `[['00b6de1c', '00b6de1f']]`
  - `CONDITIONAL_JUMP` [`00b6de1c`](#insn-00b6de1c) → [`00b6de2c`](#insn-00b6de2c)
  - `FALL_THROUGH` [`00b6de1c`](#insn-00b6de1c) → [`00b6de20`](#insn-00b6de20)
- ブロック [`00b6de20`](#insn-00b6de20) 範囲 `[['00b6de20', '00b6de2b']]`
  - `FALL_THROUGH` [`00b6de28`](#insn-00b6de28) → [`00b6de2c`](#insn-00b6de2c)
- ブロック [`00b6de2c`](#insn-00b6de2c) 範囲 `[['00b6de2c', '00b6de43']]`
- ブロック [`00b6de44`](#insn-00b6de44) 範囲 `[['00b6de44', '00b6de57']]`
  - `FALL_THROUGH` [`00b6de54`](#insn-00b6de54) → [`00b6de58`](#insn-00b6de58)
- ブロック [`00b6de58`](#insn-00b6de58) 範囲 `[['00b6de58', '00b6de63']]`
  - `CONDITIONAL_JUMP` [`00b6de60`](#insn-00b6de60) → [`00b6de80`](#insn-00b6de80)
  - `FALL_THROUGH` [`00b6de60`](#insn-00b6de60) → [`00b6de64`](#insn-00b6de64)
- ブロック [`00b6de64`](#insn-00b6de64) 範囲 `[['00b6de64', '00b6de6b']]`
  - `CONDITIONAL_JUMP` [`00b6de68`](#insn-00b6de68) → [`00b6de58`](#insn-00b6de58)
  - `FALL_THROUGH` [`00b6de68`](#insn-00b6de68) → [`00b6de6c`](#insn-00b6de6c)
- ブロック [`00b6de6c`](#insn-00b6de6c) 範囲 `[['00b6de6c', '00b6de73']]`
  - `CONDITIONAL_JUMP` [`00b6de70`](#insn-00b6de70) → [`00b6de44`](#insn-00b6de44)
  - `FALL_THROUGH` [`00b6de70`](#insn-00b6de70) → [`00b6de74`](#insn-00b6de74)
- ブロック [`00b6de74`](#insn-00b6de74) 範囲 `[['00b6de74', '00b6de7f']]`
  - `UNCONDITIONAL_JUMP` [`00b6de7c`](#insn-00b6de7c) → [`00b6de44`](#insn-00b6de44)
- ブロック [`00b6de80`](#insn-00b6de80) 範囲 `[['00b6de80', '00b6de87']]`
  - `CONDITIONAL_JUMP` [`00b6de84`](#insn-00b6de84) → [`00b6de20`](#insn-00b6de20)
  - `FALL_THROUGH` [`00b6de84`](#insn-00b6de84) → [`00b6de88`](#insn-00b6de88)
- ブロック [`00b6de88`](#insn-00b6de88) 範囲 `[['00b6de88', '00b6de8b']]`
  - `UNCONDITIONAL_JUMP` [`00b6de88`](#insn-00b6de88) → [`00b6de2c`](#insn-00b6de2c)

## 命令位置別の参照

- [`00b6ddfc`](#insn-00b6ddfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de00`](#insn-00b6de00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de04`](#insn-00b6de04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de18`](#insn-00b6de18) → [`00b6de64`](#insn-00b6de64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de1c`](#insn-00b6de1c) → [`00b6de2c`](#insn-00b6de2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de28`](#insn-00b6de28) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b6de34`](#insn-00b6de34) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de38`](#insn-00b6de38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de40`](#insn-00b6de40) → [`00c5bb60`](../00c5b/00c5bb60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb60` · 推定シンボル `None` · 推定型 `None`
- [`00b6de48`](#insn-00b6de48) → [`00c5b940`](../00c5b/00c5b940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b940` · 推定シンボル `None` · 推定型 `None`
- [`00b6de50`](#insn-00b6de50) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b6de60`](#insn-00b6de60) → [`00b6de80`](#insn-00b6de80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de68`](#insn-00b6de68) → [`00b6de58`](#insn-00b6de58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de70`](#insn-00b6de70) → [`00b6de44`](#insn-00b6de44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de78`](#insn-00b6de78) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b6de7c`](#insn-00b6de7c) → [`00b6de44`](#insn-00b6de44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de84`](#insn-00b6de84) → [`00b6de20`](#insn-00b6de20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6de88`](#insn-00b6de88) → [`00b6de2c`](#insn-00b6de2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6ddfc`](#insn-00b6ddfc)

~~~json
{
  "source": "00b6ddfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de00`](#insn-00b6de00)

~~~json
{
  "source": "00b6de00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de04`](#insn-00b6de04)

~~~json
{
  "source": "00b6de04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de18`](#insn-00b6de18)

~~~json
{
  "source": "00b6de18",
  "target": "00b6de64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de1c`](#insn-00b6de1c)

~~~json
{
  "source": "00b6de1c",
  "target": "00b6de2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de28`](#insn-00b6de28)

~~~json
{
  "source": "00b6de28",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6de34`](#insn-00b6de34)

~~~json
{
  "source": "00b6de34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de38`](#insn-00b6de38)

~~~json
{
  "source": "00b6de38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de40`](#insn-00b6de40)

~~~json
{
  "source": "00b6de40",
  "target": "00c5bb60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6de48`](#insn-00b6de48)

~~~json
{
  "source": "00b6de48",
  "target": "00c5b940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6de50`](#insn-00b6de50)

~~~json
{
  "source": "00b6de50",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6de60`](#insn-00b6de60)

~~~json
{
  "source": "00b6de60",
  "target": "00b6de80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de68`](#insn-00b6de68)

~~~json
{
  "source": "00b6de68",
  "target": "00b6de58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de70`](#insn-00b6de70)

~~~json
{
  "source": "00b6de70",
  "target": "00b6de44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de78`](#insn-00b6de78)

~~~json
{
  "source": "00b6de78",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6de7c`](#insn-00b6de7c)

~~~json
{
  "source": "00b6de7c",
  "target": "00b6de44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de84`](#insn-00b6de84)

~~~json
{
  "source": "00b6de84",
  "target": "00b6de20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6de88`](#insn-00b6de88)

~~~json
{
  "source": "00b6de88",
  "target": "00b6de2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
