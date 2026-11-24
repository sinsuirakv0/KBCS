# 004bebdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `004beb9c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beb9c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0008.md#compare-af31856286bb128235a7a6c92acccb9c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `004beefc`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004be/004beefc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0008.md#compare-d10cd7ea5fc7abd7e69e94166e3246d4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bebdc",
  "name": "_ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba4877c45772c22105358d174148cd98935cda87c0e0af005a8ebe75e854a0f6",
  "source_text_sha256": "ba4877c45772c22105358d174148cd98935cda87c0e0af005a8ebe75e854a0f6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bebdc",
        "004bec7f"
      ],
      [
        "004becac",
        "004becaf"
      ]
    ],
    "bytes_sha256": "2e5aedeb7ab03bd916cfc1a5a8c4a97fe5774c8d40f1ed482e51380a13982bac",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00459510](../00459/00459510.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58e70](../00c58/00c58e70.md)

## 関連文字列（未確認候補）

~~~text
"CPUID flags: "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 828 bytes

~~~c

void _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE(undefined8 param_1)

{
  long lVar1;
  undefined1 *puVar2;
  undefined8 uVar3;
  byte local_50;
  undefined1 auStack_4f [7];
  ulong local_48;
  undefined1 *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar3 = FUN_00459510(param_1,"CPUID flags: ",0xd);
  _ZN5Botan5CPUID9to_stringEv(&local_50);
  puVar2 = local_40;
  if ((local_50 & 1) == 0) {
    local_48 = (ulong)(local_50 >> 1);
    puVar2 = auStack_4f;
  }
  uVar3 = FUN_00459510(uVar3,puVar2,local_48);
  FUN_00459510(uVar3,&DAT_002b4c11,1);
  if ((local_50 & 1) != 0) {
    _ZdlPv(local_40);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bebdc"></a> `004bebdc` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004bebe0"></a> `004bebe0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bebe4"></a> `004bebe4` | `f5 1b 00 f9` | str x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bebe8"></a> `004bebe8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bebec"></a> `004bebec` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004bebf0"></a> `004bebf0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004bebf4"></a> `004bebf4` | `41 ef ff 90` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-004bebf8"></a> `004bebf8` | `21 b0 15 91` | add x1,x1,#0x56c | `FALL_THROUGH`
<a id="insn-004bebfc"></a> `004bebfc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004bec00"></a> `004bec00` | `a2 01 80 52` | mov w2,#0xd | `FALL_THROUGH`
<a id="insn-004bec04"></a> `004bec04` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bec08"></a> `004bec08` | `42 6a fe 97` | bl 0x00459510 | `UNCONDITIONAL_CALL`
<a id="insn-004bec0c"></a> `004bec0c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004bec10"></a> `004bec10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bec14"></a> `004bec14` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-004bec18"></a> `004bec18` | `96 68 1e 94` | bl 0x00c58e70 | `UNCONDITIONAL_CALL`
<a id="insn-004bec1c"></a> `004bec1c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004bec20"></a> `004bec20` | `ea a7 40 a9` | ldp x10,x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004bec24"></a> `004bec24` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004bec28"></a> `004bec28` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004bec2c"></a> `004bec2c` | `21 15 95 9a` | csinc x1,x9,x21,ne | `FALL_THROUGH`
<a id="insn-004bec30"></a> `004bec30` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-004bec34"></a> `004bec34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bec38"></a> `004bec38` | `36 6a fe 97` | bl 0x00459510 | `UNCONDITIONAL_CALL`
<a id="insn-004bec3c"></a> `004bec3c` | `a1 ef ff d0` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-004bec40"></a> `004bec40` | `21 44 30 91` | add x1,x1,#0xc11 | `FALL_THROUGH`
<a id="insn-004bec44"></a> `004bec44` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004bec48"></a> `004bec48` | `32 6a fe 97` | bl 0x00459510 | `UNCONDITIONAL_CALL`
<a id="insn-004bec4c"></a> `004bec4c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004bec50"></a> `004bec50` | `68 00 00 36` | tbz w8,#0x0,0x004bec5c | `CONDITIONAL_JUMP`
<a id="insn-004bec54"></a> `004bec54` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004bec58"></a> `004bec58` | `ca 64 1e 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-004bec5c"></a> `004bec5c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-004bec60"></a> `004bec60` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bec64"></a> `004bec64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bec68"></a> `004bec68` | `21 02 00 54` | b.ne 0x004becac | `CONDITIONAL_JUMP`
<a id="insn-004bec6c"></a> `004bec6c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bec70"></a> `004bec70` | `f5 1b 40 f9` | ldr x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bec74"></a> `004bec74` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bec78"></a> `004bec78` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004bec7c"></a> `004bec7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004becac"></a> `004becac` | `c1 64 1e 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bebdc`](#insn-004bebdc) 範囲 `[['004bebdc', '004bec53']]`
  - `CONDITIONAL_JUMP` [`004bec50`](#insn-004bec50) → [`004bec5c`](#insn-004bec5c)
  - `FALL_THROUGH` [`004bec50`](#insn-004bec50) → [`004bec54`](#insn-004bec54)
- ブロック [`004bec54`](#insn-004bec54) 範囲 `[['004bec54', '004bec5b']]`
  - `FALL_THROUGH` [`004bec58`](#insn-004bec58) → [`004bec5c`](#insn-004bec5c)
- ブロック [`004bec5c`](#insn-004bec5c) 範囲 `[['004bec5c', '004bec6b']]`
  - `CONDITIONAL_JUMP` [`004bec68`](#insn-004bec68) → [`004becac`](#insn-004becac)
  - `FALL_THROUGH` [`004bec68`](#insn-004bec68) → [`004bec6c`](#insn-004bec6c)
- ブロック [`004bec6c`](#insn-004bec6c) 範囲 `[['004bec6c', '004bec7f']]`
- ブロック [`004becac`](#insn-004becac) 範囲 `[['004becac', '004becaf']]`

## 命令位置別の参照

- [`004bebe0`](#insn-004bebe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bebe4`](#insn-004bebe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bebe8`](#insn-004bebe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bebf8`](#insn-004bebf8) → `002a656c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bec04`](#insn-004bec04) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec08`](#insn-004bec08) → [`00459510`](../00459/00459510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459510` · 推定シンボル `None` · 推定型 `None`
- [`004bec18`](#insn-004bec18) → [`00c58e70`](../00c58/00c58e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58e70` · 推定シンボル `None` · 推定型 `None`
- [`004bec1c`](#insn-004bec1c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec20`](#insn-004bec20) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec38`](#insn-004bec38) → [`00459510`](../00459/00459510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459510` · 推定シンボル `None` · 推定型 `None`
- [`004bec40`](#insn-004bec40) → `002b4c11`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec48`](#insn-004bec48) → [`00459510`](../00459/00459510.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459510` · 推定シンボル `None` · 推定型 `None`
- [`004bec4c`](#insn-004bec4c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec50`](#insn-004bec50) → [`004bec5c`](#insn-004bec5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec54`](#insn-004bec54) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec58`](#insn-004bec58) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`004bec60`](#insn-004bec60) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec68`](#insn-004bec68) → [`004becac`](#insn-004becac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec6c`](#insn-004bec6c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec70`](#insn-004bec70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bec74`](#insn-004bec74) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004becac`](#insn-004becac) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bebe0`](#insn-004bebe0)

~~~json
{
  "source": "004bebe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bebe4`](#insn-004bebe4)

~~~json
{
  "source": "004bebe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bebe8`](#insn-004bebe8)

~~~json
{
  "source": "004bebe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bebf8`](#insn-004bebf8)

~~~json
{
  "source": "004bebf8",
  "target": "002a656c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a656c",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "435055494420666c6167733a2000",
  "capture_start": "002a656c",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bec04`](#insn-004bec04)

~~~json
{
  "source": "004bec04",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec08`](#insn-004bec08)

~~~json
{
  "source": "004bec08",
  "target": "00459510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bec18`](#insn-004bec18)

~~~json
{
  "source": "004bec18",
  "target": "00c58e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bec1c`](#insn-004bec1c)

~~~json
{
  "source": "004bec1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec20`](#insn-004bec20)

~~~json
{
  "source": "004bec20",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec38`](#insn-004bec38)

~~~json
{
  "source": "004bec38",
  "target": "00459510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bec40`](#insn-004bec40)

~~~json
{
  "source": "004bec40",
  "target": "002b4c11",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec48`](#insn-004bec48)

~~~json
{
  "source": "004bec48",
  "target": "00459510",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bec4c`](#insn-004bec4c)

~~~json
{
  "source": "004bec4c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec50`](#insn-004bec50)

~~~json
{
  "source": "004bec50",
  "target": "004bec5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec54`](#insn-004bec54)

~~~json
{
  "source": "004bec54",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec58`](#insn-004bec58)

~~~json
{
  "source": "004bec58",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bec60`](#insn-004bec60)

~~~json
{
  "source": "004bec60",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec68`](#insn-004bec68)

~~~json
{
  "source": "004bec68",
  "target": "004becac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec6c`](#insn-004bec6c)

~~~json
{
  "source": "004bec6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec70`](#insn-004bec70)

~~~json
{
  "source": "004bec70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bec74`](#insn-004bec74)

~~~json
{
  "source": "004bec74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004becac`](#insn-004becac)

~~~json
{
  "source": "004becac",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
