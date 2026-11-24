# 00bff5ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfe5b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfe5b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-d69f8586842d39dd8997820e66ba1674)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff5ac",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f050ae492ba466fddcc8d7f4dba89eb57f0594ba0087d1e88a86f1d7bd8bc102",
  "source_text_sha256": "f050ae492ba466fddcc8d7f4dba89eb57f0594ba0087d1e88a86f1d7bd8bc102",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bff5ac",
        "00bff683"
      ]
    ],
    "bytes_sha256": "0cf621707b29f1feffbed2103b176a48259d3511c39cc7e2c7b7230acd61f843",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1033 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv(long *param_1)

{
  int iVar1;
  long *plVar2;
  long lVar3;
  uint uVar4;
  char local_24 [4];
  
  lVar3 = *(long *)(*param_1 + -0x18);
  param_1[1] = 0;
  uVar4 = *(uint *)((long)param_1 + lVar3 + 0x20) & 0xfffffffd;
  _ZNSt6__ndk18ios_base5clearEj((long)param_1 + *(long *)(*param_1 + -0x18),uVar4);
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    uVar4 = uVar4 | 4;
    goto LAB_00bff654;
  }
  plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
  if (plVar2 != (long *)0x0) {
    if (plVar2[2] != plVar2[3]) {
      plVar2[3] = plVar2[3] + -1;
      goto LAB_00bff654;
    }
    iVar1 = (**(code **)(*plVar2 + 0x58))(plVar2,0xffffffff);
    if (iVar1 != -1) goto LAB_00bff654;
  }
  uVar4 = uVar4 | 1;
LAB_00bff654:
  lVar3 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar3,*(uint *)(lVar3 + 0x20) | uVar4);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bff5ac"></a> `00bff5ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bff5b0"></a> `00bff5b0` | `ff c3 00 d1` | sub sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bff5b4"></a> `00bff5b4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff5b8"></a> `00bff5b8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bff5bc"></a> `00bff5bc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bff5c0"></a> `00bff5c0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bff5c4"></a> `00bff5c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bff5c8"></a> `00bff5c8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff5cc"></a> `00bff5cc` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bff5d0"></a> `00bff5d0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff5d4"></a> `00bff5d4` | `09 00 09 8b` | add x9,x0,x9 | `FALL_THROUGH`
<a id="insn-00bff5d8"></a> `00bff5d8` | `29 21 40 b9` | ldr w9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bff5dc"></a> `00bff5dc` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bff5e0"></a> `00bff5e0` | `34 79 1e 12` | and w20,w9,#0xfffffffd | `FALL_THROUGH`
<a id="insn-00bff5e4"></a> `00bff5e4` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00bff5e8"></a> `00bff5e8` | `56 67 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bff5ec"></a> `00bff5ec` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bff5f0"></a> `00bff5f0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bff5f4"></a> `00bff5f4` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bff5f8"></a> `00bff5f8` | `1e 6e 01 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bff5fc"></a> `00bff5fc` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bff600"></a> `00bff600` | `88 01 00 34` | cbz w8,0x00bff630 | `CONDITIONAL_JUMP`
<a id="insn-00bff604"></a> `00bff604` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bff608"></a> `00bff608` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff60c"></a> `00bff60c` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bff610"></a> `00bff610` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bff614"></a> `00bff614` | `e0 01 00 b4` | cbz x0,0x00bff650 | `CONDITIONAL_JUMP`
<a id="insn-00bff618"></a> `00bff618` | `09 20 41 a9` | ldp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bff61c"></a> `00bff61c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bff620"></a> `00bff620` | `c0 00 00 54` | b.eq 0x00bff638 | `CONDITIONAL_JUMP`
<a id="insn-00bff624"></a> `00bff624` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bff628"></a> `00bff628` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bff62c"></a> `00bff62c` | `0a 00 00 14` | b 0x00bff654 | `UNCONDITIONAL_JUMP`
<a id="insn-00bff630"></a> `00bff630` | `94 02 1e 32` | orr w20,w20,#0x4 | `FALL_THROUGH`
<a id="insn-00bff634"></a> `00bff634` | `08 00 00 14` | b 0x00bff654 | `UNCONDITIONAL_JUMP`
<a id="insn-00bff638"></a> `00bff638` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bff63c"></a> `00bff63c` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00bff640"></a> `00bff640` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bff644"></a> `00bff644` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bff648"></a> `00bff648` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bff64c"></a> `00bff64c` | `41 00 00 54` | b.ne 0x00bff654 | `CONDITIONAL_JUMP`
<a id="insn-00bff650"></a> `00bff650` | `94 02 00 32` | orr w20,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bff654"></a> `00bff654` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bff658"></a> `00bff658` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff65c"></a> `00bff65c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bff660"></a> `00bff660` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bff664"></a> `00bff664` | `01 01 14 2a` | orr w1,w8,w20 | `FALL_THROUGH`
<a id="insn-00bff668"></a> `00bff668` | `36 67 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bff66c"></a> `00bff66c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bff670"></a> `00bff670` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bff674"></a> `00bff674` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bff678"></a> `00bff678` | `ff c3 00 91` | add sp,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bff67c"></a> `00bff67c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bff680"></a> `00bff680` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bff5ac`](#insn-00bff5ac) 範囲 `[['00bff5ac', '00bff603']]`
  - `CONDITIONAL_JUMP` [`00bff600`](#insn-00bff600) → [`00bff630`](#insn-00bff630)
  - `FALL_THROUGH` [`00bff600`](#insn-00bff600) → [`00bff604`](#insn-00bff604)
- ブロック [`00bff604`](#insn-00bff604) 範囲 `[['00bff604', '00bff617']]`
  - `CONDITIONAL_JUMP` [`00bff614`](#insn-00bff614) → [`00bff650`](#insn-00bff650)
  - `FALL_THROUGH` [`00bff614`](#insn-00bff614) → [`00bff618`](#insn-00bff618)
- ブロック [`00bff618`](#insn-00bff618) 範囲 `[['00bff618', '00bff623']]`
  - `CONDITIONAL_JUMP` [`00bff620`](#insn-00bff620) → [`00bff638`](#insn-00bff638)
  - `FALL_THROUGH` [`00bff620`](#insn-00bff620) → [`00bff624`](#insn-00bff624)
- ブロック [`00bff624`](#insn-00bff624) 範囲 `[['00bff624', '00bff62f']]`
  - `UNCONDITIONAL_JUMP` [`00bff62c`](#insn-00bff62c) → [`00bff654`](#insn-00bff654)
- ブロック [`00bff630`](#insn-00bff630) 範囲 `[['00bff630', '00bff637']]`
  - `UNCONDITIONAL_JUMP` [`00bff634`](#insn-00bff634) → [`00bff654`](#insn-00bff654)
- ブロック [`00bff638`](#insn-00bff638) 範囲 `[['00bff638', '00bff64f']]`
  - `CONDITIONAL_JUMP` [`00bff64c`](#insn-00bff64c) → [`00bff654`](#insn-00bff654)
  - `FALL_THROUGH` [`00bff64c`](#insn-00bff64c) → [`00bff650`](#insn-00bff650)
- ブロック [`00bff650`](#insn-00bff650) 範囲 `[['00bff650', '00bff653']]`
  - `FALL_THROUGH` [`00bff650`](#insn-00bff650) → [`00bff654`](#insn-00bff654)
- ブロック [`00bff654`](#insn-00bff654) 範囲 `[['00bff654', '00bff683']]`

## 命令位置別の参照

- [`00bff5b4`](#insn-00bff5b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff5b8`](#insn-00bff5b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff5e8`](#insn-00bff5e8) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bff5f8`](#insn-00bff5f8) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bff5fc`](#insn-00bff5fc) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff600`](#insn-00bff600) → [`00bff630`](#insn-00bff630) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff614`](#insn-00bff614) → [`00bff650`](#insn-00bff650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff620`](#insn-00bff620) → [`00bff638`](#insn-00bff638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff62c`](#insn-00bff62c) → [`00bff654`](#insn-00bff654) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff634`](#insn-00bff634) → [`00bff654`](#insn-00bff654) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff64c`](#insn-00bff64c) → [`00bff654`](#insn-00bff654) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff668`](#insn-00bff668) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bff670`](#insn-00bff670) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff674`](#insn-00bff674) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bff5b4`](#insn-00bff5b4)

~~~json
{
  "source": "00bff5b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff5b8`](#insn-00bff5b8)

~~~json
{
  "source": "00bff5b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff5e8`](#insn-00bff5e8)

~~~json
{
  "source": "00bff5e8",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff5f8`](#insn-00bff5f8)

~~~json
{
  "source": "00bff5f8",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff5fc`](#insn-00bff5fc)

~~~json
{
  "source": "00bff5fc",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff600`](#insn-00bff600)

~~~json
{
  "source": "00bff600",
  "target": "00bff630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff614`](#insn-00bff614)

~~~json
{
  "source": "00bff614",
  "target": "00bff650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff620`](#insn-00bff620)

~~~json
{
  "source": "00bff620",
  "target": "00bff638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff62c`](#insn-00bff62c)

~~~json
{
  "source": "00bff62c",
  "target": "00bff654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff634`](#insn-00bff634)

~~~json
{
  "source": "00bff634",
  "target": "00bff654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff64c`](#insn-00bff64c)

~~~json
{
  "source": "00bff64c",
  "target": "00bff654",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff668`](#insn-00bff668)

~~~json
{
  "source": "00bff668",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff670`](#insn-00bff670)

~~~json
{
  "source": "00bff670",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff674`](#insn-00bff674)

~~~json
{
  "source": "00bff674",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
