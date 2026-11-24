# 00bad7fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bad7b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bad7b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-115137f2c43843ea26bd9b65c9bd1e52)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2a244`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a244.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0006.md#compare-20478667d2cd5ad9ff140b38d8436ceb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bad7fc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb0EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "482c9c8351539c0a3f32d0d15480fc08863aebeb44c9132f2f96aebbf6138cdb",
  "source_text_sha256": "482c9c8351539c0a3f32d0d15480fc08863aebeb44c9132f2f96aebbf6138cdb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bad7fc",
        "00bad8df"
      ]
    ],
    "bytes_sha256": "37b1b9437e56566e6898749b2bc7bee8dd74d9f104c1626e44f0604fb7419834",
    "instruction_count": 57,
    "instruction_bytes": 228,
    "body_bytes": 228,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1450 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IwLb0EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  int iVar1;
  uint uVar2;
  byte bVar3;
  undefined8 uVar4;
  ulong uVar5;
  byte *pbVar6;
  long lVar7;
  
  uVar5 = *(ulong *)(param_1 + 0x18);
  if ((*(byte *)(param_1 + 0x20) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00bad818:
      uVar4 = 1;
      goto LAB_00bad8d4;
    }
    param_6[0] = 0xfe;
    param_6[1] = 0xff;
    param_6 = param_6 + 2;
  }
  for (; param_3 < param_4; param_3 = param_3 + 1) {
    uVar2 = *param_3;
    if (uVar2 >> 0xb == 0x1b || uVar5 < uVar2) {
      uVar4 = 2;
      goto LAB_00bad8d4;
    }
    bVar3 = (byte)(uVar2 >> 8);
    if (uVar2 >> 0x10 == 0) {
      if (param_7 - (long)param_6 < 2) goto LAB_00bad818;
      pbVar6 = param_6 + 1;
      *param_6 = bVar3;
      lVar7 = 2;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00bad818;
      iVar1 = (uVar2 >> 10 & 0x7c0) + 0x3fc0;
      param_6[2] = bVar3 & 3 | 0xdc;
      *param_6 = (byte)((uint)iVar1 >> 8) | 0xd8;
      lVar7 = 4;
      param_6[1] = (byte)iVar1 | (byte)(uVar2 >> 10) & 0x3f;
      pbVar6 = param_6 + 3;
    }
    *pbVar6 = (byte)uVar2;
    param_6 = param_6 + lVar7;
  }
  uVar4 = 0;
LAB_00bad8d4:
  *param_5 = param_3;
  *param_8 = param_6;
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bad7fc"></a> `00bad7fc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bad800"></a> `00bad800` | `09 80 40 39` | ldrb w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bad804"></a> `00bad804` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bad808"></a> `00bad808` | `09 01 08 36` | tbz w9,#0x1,0x00bad828 | `CONDITIONAL_JUMP`
<a id="insn-00bad80c"></a> `00bad80c` | `c9 00 05 cb` | sub x9,x6,x5 | `FALL_THROUGH`
<a id="insn-00bad810"></a> `00bad810` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bad814"></a> `00bad814` | `6a 00 00 54` | b.ge 0x00bad820 | `CONDITIONAL_JUMP`
<a id="insn-00bad818"></a> `00bad818` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bad81c"></a> `00bad81c` | `2e 00 00 14` | b 0x00bad8d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad820"></a> `00bad820` | `c9 ff 9f 52` | mov w9,#0xfffe | `FALL_THROUGH`
<a id="insn-00bad824"></a> `00bad824` | `a9 24 00 78` | strh w9,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00bad828"></a> `00bad828` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bad82c"></a> `00bad82c` | `e2 04 00 54` | b.cs 0x00bad8c8 | `CONDITIONAL_JUMP`
<a id="insn-00bad830"></a> `00bad830` | `09 f8 87 52` | mov w9,#0x3fc0 | `FALL_THROUGH`
<a id="insn-00bad834"></a> `00bad834` | `0a 1b 80 52` | mov w10,#0xd8 | `FALL_THROUGH`
<a id="insn-00bad838"></a> `00bad838` | `06 00 00 14` | b 0x00bad850 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad83c"></a> `00bad83c` | `42 10 00 91` | add x2,x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bad840"></a> `00bad840` | `a5 00 0d 8b` | add x5,x5,x13 | `FALL_THROUGH`
<a id="insn-00bad844"></a> `00bad844` | `8b 01 00 39` | strb w11,[x12] | `FALL_THROUGH`
<a id="insn-00bad848"></a> `00bad848` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bad84c"></a> `00bad84c` | `e2 03 00 54` | b.cs 0x00bad8c8 | `CONDITIONAL_JUMP`
<a id="insn-00bad850"></a> `00bad850` | `4b 00 40 b9` | ldr w11,[x2] | `FALL_THROUGH`
<a id="insn-00bad854"></a> `00bad854` | `6c 7d 0b 53` | lsr w12,w11,#0xb | `FALL_THROUGH`
<a id="insn-00bad858"></a> `00bad858` | `9f 6d 00 71` | cmp w12,#0x1b | `FALL_THROUGH`
<a id="insn-00bad85c"></a> `00bad85c` | `00 11 4b fa` | ccmp x8,x11,#0x0,ne | `FALL_THROUGH`
<a id="insn-00bad860"></a> `00bad860` | `83 03 00 54` | b.cc 0x00bad8d0 | `CONDITIONAL_JUMP`
<a id="insn-00bad864"></a> `00bad864` | `6d 7d 10 53` | lsr w13,w11,#0x10 | `FALL_THROUGH`
<a id="insn-00bad868"></a> `00bad868` | `cc 00 05 cb` | sub x12,x6,x5 | `FALL_THROUGH`
<a id="insn-00bad86c"></a> `00bad86c` | `0d 01 00 35` | cbnz w13,0x00bad88c | `CONDITIONAL_JUMP`
<a id="insn-00bad870"></a> `00bad870` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bad874"></a> `00bad874` | `2b fd ff 54` | b.lt 0x00bad818 | `CONDITIONAL_JUMP`
<a id="insn-00bad878"></a> `00bad878` | `6d 7d 08 53` | lsr w13,w11,#0x8 | `FALL_THROUGH`
<a id="insn-00bad87c"></a> `00bad87c` | `ec 03 05 aa` | mov x12,x5 | `FALL_THROUGH`
<a id="insn-00bad880"></a> `00bad880` | `8d 15 00 38` | strb w13,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-00bad884"></a> `00bad884` | `4d 00 80 52` | mov w13,#0x2 | `FALL_THROUGH`
<a id="insn-00bad888"></a> `00bad888` | `ed ff ff 17` | b 0x00bad83c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad88c"></a> `00bad88c` | `9f 11 00 f1` | cmp x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bad890"></a> `00bad890` | `4b fc ff 54` | b.lt 0x00bad818 | `CONDITIONAL_JUMP`
<a id="insn-00bad894"></a> `00bad894` | `6c 7d 0a 53` | lsr w12,w11,#0xa | `FALL_THROUGH`
<a id="insn-00bad898"></a> `00bad898` | `8e 1b 80 52` | mov w14,#0xdc | `FALL_THROUGH`
<a id="insn-00bad89c"></a> `00bad89c` | `6e 25 08 33` | bfxil w14,w11,#0x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bad8a0"></a> `00bad8a0` | `8c 11 1a 12` | and w12,w12,#0x7c0 | `FALL_THROUGH`
<a id="insn-00bad8a4"></a> `00bad8a4` | `8c 01 09 0b` | add w12,w12,w9 | `FALL_THROUGH`
<a id="insn-00bad8a8"></a> `00bad8a8` | `ae 08 00 39` | strb w14,[x5, #0x2] | `FALL_THROUGH`
<a id="insn-00bad8ac"></a> `00bad8ac` | `4d 21 4c 2a` | orr w13,w10,w12, LSR #0x8 | `FALL_THROUGH`
<a id="insn-00bad8b0"></a> `00bad8b0` | `6c 3d 0a 33` | bfxil w12,w11,#0xa,#0x6 | `FALL_THROUGH`
<a id="insn-00bad8b4"></a> `00bad8b4` | `ad 00 00 39` | strb w13,[x5] | `FALL_THROUGH`
<a id="insn-00bad8b8"></a> `00bad8b8` | `8d 00 80 52` | mov w13,#0x4 | `FALL_THROUGH`
<a id="insn-00bad8bc"></a> `00bad8bc` | `ac 04 00 39` | strb w12,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00bad8c0"></a> `00bad8c0` | `ac 0c 00 91` | add x12,x5,#0x3 | `FALL_THROUGH`
<a id="insn-00bad8c4"></a> `00bad8c4` | `de ff ff 17` | b 0x00bad83c | `UNCONDITIONAL_JUMP`
<a id="insn-00bad8c8"></a> `00bad8c8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bad8cc"></a> `00bad8cc` | `02 00 00 14` | b 0x00bad8d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad8d0"></a> `00bad8d0` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bad8d4"></a> `00bad8d4` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00bad8d8"></a> `00bad8d8` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00bad8dc"></a> `00bad8dc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bad7fc`](#insn-00bad7fc) 範囲 `[['00bad7fc', '00bad80b']]`
  - `CONDITIONAL_JUMP` [`00bad808`](#insn-00bad808) → [`00bad828`](#insn-00bad828)
  - `FALL_THROUGH` [`00bad808`](#insn-00bad808) → [`00bad80c`](#insn-00bad80c)
- ブロック [`00bad80c`](#insn-00bad80c) 範囲 `[['00bad80c', '00bad817']]`
  - `CONDITIONAL_JUMP` [`00bad814`](#insn-00bad814) → [`00bad820`](#insn-00bad820)
  - `FALL_THROUGH` [`00bad814`](#insn-00bad814) → [`00bad818`](#insn-00bad818)
- ブロック [`00bad818`](#insn-00bad818) 範囲 `[['00bad818', '00bad81f']]`
  - `UNCONDITIONAL_JUMP` [`00bad81c`](#insn-00bad81c) → [`00bad8d4`](#insn-00bad8d4)
- ブロック [`00bad820`](#insn-00bad820) 範囲 `[['00bad820', '00bad827']]`
  - `FALL_THROUGH` [`00bad824`](#insn-00bad824) → [`00bad828`](#insn-00bad828)
- ブロック [`00bad828`](#insn-00bad828) 範囲 `[['00bad828', '00bad82f']]`
  - `CONDITIONAL_JUMP` [`00bad82c`](#insn-00bad82c) → [`00bad8c8`](#insn-00bad8c8)
  - `FALL_THROUGH` [`00bad82c`](#insn-00bad82c) → [`00bad830`](#insn-00bad830)
- ブロック [`00bad830`](#insn-00bad830) 範囲 `[['00bad830', '00bad83b']]`
  - `UNCONDITIONAL_JUMP` [`00bad838`](#insn-00bad838) → [`00bad850`](#insn-00bad850)
- ブロック [`00bad83c`](#insn-00bad83c) 範囲 `[['00bad83c', '00bad84f']]`
  - `CONDITIONAL_JUMP` [`00bad84c`](#insn-00bad84c) → [`00bad8c8`](#insn-00bad8c8)
  - `FALL_THROUGH` [`00bad84c`](#insn-00bad84c) → [`00bad850`](#insn-00bad850)
- ブロック [`00bad850`](#insn-00bad850) 範囲 `[['00bad850', '00bad863']]`
  - `CONDITIONAL_JUMP` [`00bad860`](#insn-00bad860) → [`00bad8d0`](#insn-00bad8d0)
  - `FALL_THROUGH` [`00bad860`](#insn-00bad860) → [`00bad864`](#insn-00bad864)
- ブロック [`00bad864`](#insn-00bad864) 範囲 `[['00bad864', '00bad86f']]`
  - `CONDITIONAL_JUMP` [`00bad86c`](#insn-00bad86c) → [`00bad88c`](#insn-00bad88c)
  - `FALL_THROUGH` [`00bad86c`](#insn-00bad86c) → [`00bad870`](#insn-00bad870)
- ブロック [`00bad870`](#insn-00bad870) 範囲 `[['00bad870', '00bad877']]`
  - `CONDITIONAL_JUMP` [`00bad874`](#insn-00bad874) → [`00bad818`](#insn-00bad818)
  - `FALL_THROUGH` [`00bad874`](#insn-00bad874) → [`00bad878`](#insn-00bad878)
- ブロック [`00bad878`](#insn-00bad878) 範囲 `[['00bad878', '00bad88b']]`
  - `UNCONDITIONAL_JUMP` [`00bad888`](#insn-00bad888) → [`00bad83c`](#insn-00bad83c)
- ブロック [`00bad88c`](#insn-00bad88c) 範囲 `[['00bad88c', '00bad893']]`
  - `CONDITIONAL_JUMP` [`00bad890`](#insn-00bad890) → [`00bad818`](#insn-00bad818)
  - `FALL_THROUGH` [`00bad890`](#insn-00bad890) → [`00bad894`](#insn-00bad894)
- ブロック [`00bad894`](#insn-00bad894) 範囲 `[['00bad894', '00bad8c7']]`
  - `UNCONDITIONAL_JUMP` [`00bad8c4`](#insn-00bad8c4) → [`00bad83c`](#insn-00bad83c)
- ブロック [`00bad8c8`](#insn-00bad8c8) 範囲 `[['00bad8c8', '00bad8cf']]`
  - `UNCONDITIONAL_JUMP` [`00bad8cc`](#insn-00bad8cc) → [`00bad8d4`](#insn-00bad8d4)
- ブロック [`00bad8d0`](#insn-00bad8d0) 範囲 `[['00bad8d0', '00bad8d3']]`
  - `FALL_THROUGH` [`00bad8d0`](#insn-00bad8d0) → [`00bad8d4`](#insn-00bad8d4)
- ブロック [`00bad8d4`](#insn-00bad8d4) 範囲 `[['00bad8d4', '00bad8df']]`

## 命令位置別の参照

- [`00bad808`](#insn-00bad808) → [`00bad828`](#insn-00bad828) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad814`](#insn-00bad814) → [`00bad820`](#insn-00bad820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad81c`](#insn-00bad81c) → [`00bad8d4`](#insn-00bad8d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad82c`](#insn-00bad82c) → [`00bad8c8`](#insn-00bad8c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad838`](#insn-00bad838) → [`00bad850`](#insn-00bad850) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad84c`](#insn-00bad84c) → [`00bad8c8`](#insn-00bad8c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad860`](#insn-00bad860) → [`00bad8d0`](#insn-00bad8d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad86c`](#insn-00bad86c) → [`00bad88c`](#insn-00bad88c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad874`](#insn-00bad874) → [`00bad818`](#insn-00bad818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad888`](#insn-00bad888) → [`00bad83c`](#insn-00bad83c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad890`](#insn-00bad890) → [`00bad818`](#insn-00bad818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8c4`](#insn-00bad8c4) → [`00bad83c`](#insn-00bad83c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad8cc`](#insn-00bad8cc) → [`00bad8d4`](#insn-00bad8d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bad808`](#insn-00bad808)

~~~json
{
  "source": "00bad808",
  "target": "00bad828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad814`](#insn-00bad814)

~~~json
{
  "source": "00bad814",
  "target": "00bad820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad81c`](#insn-00bad81c)

~~~json
{
  "source": "00bad81c",
  "target": "00bad8d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad82c`](#insn-00bad82c)

~~~json
{
  "source": "00bad82c",
  "target": "00bad8c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad838`](#insn-00bad838)

~~~json
{
  "source": "00bad838",
  "target": "00bad850",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad84c`](#insn-00bad84c)

~~~json
{
  "source": "00bad84c",
  "target": "00bad8c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad860`](#insn-00bad860)

~~~json
{
  "source": "00bad860",
  "target": "00bad8d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad86c`](#insn-00bad86c)

~~~json
{
  "source": "00bad86c",
  "target": "00bad88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad874`](#insn-00bad874)

~~~json
{
  "source": "00bad874",
  "target": "00bad818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad888`](#insn-00bad888)

~~~json
{
  "source": "00bad888",
  "target": "00bad83c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad890`](#insn-00bad890)

~~~json
{
  "source": "00bad890",
  "target": "00bad818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8c4`](#insn-00bad8c4)

~~~json
{
  "source": "00bad8c4",
  "target": "00bad83c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad8cc`](#insn-00bad8cc)

~~~json
{
  "source": "00bad8cc",
  "target": "00bad8d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
