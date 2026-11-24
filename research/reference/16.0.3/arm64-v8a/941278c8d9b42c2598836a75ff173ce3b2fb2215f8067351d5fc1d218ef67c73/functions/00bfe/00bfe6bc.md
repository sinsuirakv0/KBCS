# 00bfe6bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfd6c8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfd6c8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-5e9d0da3a4dfa7175a8e7cd0f1d7b8f1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfe6bc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5de0382271c7a8fb7241d6abc2f5a2681149235814834513e200ad9378db4cea",
  "source_text_sha256": "5de0382271c7a8fb7241d6abc2f5a2681149235814834513e200ad9378db4cea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfe6bc",
        "00bfe77f"
      ]
    ],
    "bytes_sha256": "414311f98c373a3c09cfa6a7c081f46d46222e7233aa68dec2fa85070f6f2c9c",
    "instruction_count": 49,
    "instruction_bytes": 196,
    "body_bytes": 196,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5f400](../00c5f/00c5f400.md)

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 879 bytes

~~~c

uint _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv(long *param_1)

{
  long lVar1;
  byte *pbVar2;
  long *plVar3;
  uint uVar4;
  uint uVar5;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    return 0xffffffff;
  }
  plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
  pbVar2 = (byte *)plVar3[3];
  if (pbVar2 == (byte *)plVar3[4]) {
    uVar5 = (**(code **)(*plVar3 + 0x50))();
    if (uVar5 == 0xffffffff) {
      uVar4 = 6;
      goto LAB_00bfe748;
    }
  }
  else {
    plVar3[3] = (long)(pbVar2 + 1);
    uVar5 = (uint)*pbVar2;
  }
  uVar4 = 0;
  param_1[1] = 1;
LAB_00bfe748:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar4);
  return uVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfe6bc"></a> `00bfe6bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfe6c0"></a> `00bfe6c0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfe6c4"></a> `00bfe6c4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe6c8"></a> `00bfe6c8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe6cc"></a> `00bfe6cc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfe6d0"></a> `00bfe6d0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfe6d4"></a> `00bfe6d4` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfe6d8"></a> `00bfe6d8` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfe6dc"></a> `00bfe6dc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfe6e0"></a> `00bfe6e0` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe6e4"></a> `00bfe6e4` | `e3 71 01 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe6e8"></a> `00bfe6e8` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfe6ec"></a> `00bfe6ec` | `88 01 00 34` | cbz w8,0x00bfe71c | `CONDITIONAL_JUMP`
<a id="insn-00bfe6f0"></a> `00bfe6f0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfe6f4"></a> `00bfe6f4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe6f8"></a> `00bfe6f8` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfe6fc"></a> `00bfe6fc` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfe700"></a> `00bfe700` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfe704"></a> `00bfe704` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfe708"></a> `00bfe708` | `e0 00 00 54` | b.eq 0x00bfe724 | `CONDITIONAL_JUMP`
<a id="insn-00bfe70c"></a> `00bfe70c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe710"></a> `00bfe710` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfe714"></a> `00bfe714` | `14 01 40 39` | ldrb w20,[x8] | `FALL_THROUGH`
<a id="insn-00bfe718"></a> `00bfe718` | `09 00 00 14` | b 0x00bfe73c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfe71c"></a> `00bfe71c` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bfe720"></a> `00bfe720` | `10 00 00 14` | b 0x00bfe760 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfe724"></a> `00bfe724` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfe728"></a> `00bfe728` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfe72c"></a> `00bfe72c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfe730"></a> `00bfe730` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bfe734"></a> `00bfe734` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe738"></a> `00bfe738` | `00 02 00 54` | b.eq 0x00bfe778 | `CONDITIONAL_JUMP`
<a id="insn-00bfe73c"></a> `00bfe73c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfe740"></a> `00bfe740` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfe744"></a> `00bfe744` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfe748"></a> `00bfe748` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfe74c"></a> `00bfe74c` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe750"></a> `00bfe750` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfe754"></a> `00bfe754` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe758"></a> `00bfe758` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfe75c"></a> `00bfe75c` | `f9 6a 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe760"></a> `00bfe760` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00bfe764"></a> `00bfe764` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe768"></a> `00bfe768` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe76c"></a> `00bfe76c` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bfe770"></a> `00bfe770` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfe774"></a> `00bfe774` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfe778"></a> `00bfe778` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00bfe77c"></a> `00bfe77c` | `f3 ff ff 17` | b 0x00bfe748 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfe6bc`](#insn-00bfe6bc) 範囲 `[['00bfe6bc', '00bfe6ef']]`
  - `CONDITIONAL_JUMP` [`00bfe6ec`](#insn-00bfe6ec) → [`00bfe71c`](#insn-00bfe71c)
  - `FALL_THROUGH` [`00bfe6ec`](#insn-00bfe6ec) → [`00bfe6f0`](#insn-00bfe6f0)
- ブロック [`00bfe6f0`](#insn-00bfe6f0) 範囲 `[['00bfe6f0', '00bfe70b']]`
  - `CONDITIONAL_JUMP` [`00bfe708`](#insn-00bfe708) → [`00bfe724`](#insn-00bfe724)
  - `FALL_THROUGH` [`00bfe708`](#insn-00bfe708) → [`00bfe70c`](#insn-00bfe70c)
- ブロック [`00bfe70c`](#insn-00bfe70c) 範囲 `[['00bfe70c', '00bfe71b']]`
  - `UNCONDITIONAL_JUMP` [`00bfe718`](#insn-00bfe718) → [`00bfe73c`](#insn-00bfe73c)
- ブロック [`00bfe71c`](#insn-00bfe71c) 範囲 `[['00bfe71c', '00bfe723']]`
  - `UNCONDITIONAL_JUMP` [`00bfe720`](#insn-00bfe720) → [`00bfe760`](#insn-00bfe760)
- ブロック [`00bfe724`](#insn-00bfe724) 範囲 `[['00bfe724', '00bfe73b']]`
  - `CONDITIONAL_JUMP` [`00bfe738`](#insn-00bfe738) → [`00bfe778`](#insn-00bfe778)
  - `FALL_THROUGH` [`00bfe738`](#insn-00bfe738) → [`00bfe73c`](#insn-00bfe73c)
- ブロック [`00bfe73c`](#insn-00bfe73c) 範囲 `[['00bfe73c', '00bfe747']]`
  - `FALL_THROUGH` [`00bfe744`](#insn-00bfe744) → [`00bfe748`](#insn-00bfe748)
- ブロック [`00bfe748`](#insn-00bfe748) 範囲 `[['00bfe748', '00bfe75f']]`
  - `FALL_THROUGH` [`00bfe75c`](#insn-00bfe75c) → [`00bfe760`](#insn-00bfe760)
- ブロック [`00bfe760`](#insn-00bfe760) 範囲 `[['00bfe760', '00bfe777']]`
- ブロック [`00bfe778`](#insn-00bfe778) 範囲 `[['00bfe778', '00bfe77f']]`
  - `UNCONDITIONAL_JUMP` [`00bfe77c`](#insn-00bfe77c) → [`00bfe748`](#insn-00bfe748)

## 命令位置別の参照

- [`00bfe6c4`](#insn-00bfe6c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe6c8`](#insn-00bfe6c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe6e4`](#insn-00bfe6e4) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bfe6e8`](#insn-00bfe6e8) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe6ec`](#insn-00bfe6ec) → [`00bfe71c`](#insn-00bfe71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe708`](#insn-00bfe708) → [`00bfe724`](#insn-00bfe724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe718`](#insn-00bfe718) → [`00bfe73c`](#insn-00bfe73c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe720`](#insn-00bfe720) → [`00bfe760`](#insn-00bfe760) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe738`](#insn-00bfe738) → [`00bfe778`](#insn-00bfe778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe75c`](#insn-00bfe75c) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bfe764`](#insn-00bfe764) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe768`](#insn-00bfe768) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe77c`](#insn-00bfe77c) → [`00bfe748`](#insn-00bfe748) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfe6c4`](#insn-00bfe6c4)

~~~json
{
  "source": "00bfe6c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe6c8`](#insn-00bfe6c8)

~~~json
{
  "source": "00bfe6c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe6e4`](#insn-00bfe6e4)

~~~json
{
  "source": "00bfe6e4",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe6e8`](#insn-00bfe6e8)

~~~json
{
  "source": "00bfe6e8",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe6ec`](#insn-00bfe6ec)

~~~json
{
  "source": "00bfe6ec",
  "target": "00bfe71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe708`](#insn-00bfe708)

~~~json
{
  "source": "00bfe708",
  "target": "00bfe724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe718`](#insn-00bfe718)

~~~json
{
  "source": "00bfe718",
  "target": "00bfe73c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe720`](#insn-00bfe720)

~~~json
{
  "source": "00bfe720",
  "target": "00bfe760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe738`](#insn-00bfe738)

~~~json
{
  "source": "00bfe738",
  "target": "00bfe778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe75c`](#insn-00bfe75c)

~~~json
{
  "source": "00bfe75c",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe764`](#insn-00bfe764)

~~~json
{
  "source": "00bfe764",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe768`](#insn-00bfe768)

~~~json
{
  "source": "00bfe768",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe77c`](#insn-00bfe77c)

~~~json
{
  "source": "00bfe77c",
  "target": "00bfe748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
