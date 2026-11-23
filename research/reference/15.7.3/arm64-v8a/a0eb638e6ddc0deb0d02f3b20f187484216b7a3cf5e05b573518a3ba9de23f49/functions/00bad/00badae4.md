# 00badae4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bada1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bada1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-0fea35f939e55c52ebfc999aeca59f01)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00badb28`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badb28.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-d4acc20b8715865debadf551ef6c9a0b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badae4",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef01bcc00a1e68fae0c24df86f81f27bc0bef0f8373635c5a7fa9a621a96f12b",
  "source_text_sha256": "ef01bcc00a1e68fae0c24df86f81f27bc0bef0f8373635c5a7fa9a621a96f12b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badae4",
        "00badbb7"
      ]
    ],
    "bytes_sha256": "06c671ab25216d05790a04a670c179d698088658f0e39e259f71bb1c68eb9041",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
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

## 疑似コード / UTF-8 1388 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  int iVar1;
  uint uVar2;
  undefined8 uVar3;
  byte *pbVar4;
  ulong uVar5;
  
  uVar5 = *(ulong *)(param_1 + 0x18);
  if ((*(byte *)(param_1 + 0x20) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00badb00:
      uVar3 = 1;
      goto LAB_00badbac;
    }
    param_6[0] = 0xff;
    param_6[1] = 0xfe;
    param_6 = param_6 + 2;
  }
  for (; param_3 < param_4; param_3 = param_3 + 1) {
    uVar2 = *param_3;
    if (uVar2 >> 0xb == 0x1b || uVar5 < uVar2) {
      uVar3 = 2;
      goto LAB_00badbac;
    }
    if ((uVar2 & 0xffff0000) == 0) {
      if (param_7 - (long)param_6 < 2) goto LAB_00badb00;
      pbVar4 = param_6 + 2;
      *(short *)param_6 = (short)uVar2;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00badb00;
      param_6[2] = (byte)uVar2;
      iVar1 = (uVar2 >> 10 & 0x7c0) + 0x3fc0;
      param_6[3] = (byte)(uVar2 >> 8) & 3 | 0xdc;
      pbVar4 = param_6 + 4;
      *param_6 = (byte)iVar1 | (byte)(uVar2 >> 10) & 0x3f;
      param_6[1] = (byte)((uint)iVar1 >> 8) | 0xd8;
    }
    param_6 = pbVar4;
  }
  uVar3 = 0;
LAB_00badbac:
  *param_5 = param_3;
  *param_8 = param_6;
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badae4"></a> `00badae4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badae8"></a> `00badae8` | `09 80 40 39` | ldrb w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00badaec"></a> `00badaec` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badaf0"></a> `00badaf0` | `09 01 08 36` | tbz w9,#0x1,0x00badb10 | `CONDITIONAL_JUMP`
<a id="insn-00badaf4"></a> `00badaf4` | `c9 00 05 cb` | sub x9,x6,x5 | `FALL_THROUGH`
<a id="insn-00badaf8"></a> `00badaf8` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00badafc"></a> `00badafc` | `6a 00 00 54` | b.ge 0x00badb08 | `CONDITIONAL_JUMP`
<a id="insn-00badb00"></a> `00badb00` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00badb04"></a> `00badb04` | `2a 00 00 14` | b 0x00badbac | `UNCONDITIONAL_JUMP`
<a id="insn-00badb08"></a> `00badb08` | `e9 df 9f 52` | mov w9,#0xfeff | `FALL_THROUGH`
<a id="insn-00badb0c"></a> `00badb0c` | `a9 24 00 78` | strh w9,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00badb10"></a> `00badb10` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badb14"></a> `00badb14` | `62 04 00 54` | b.cs 0x00badba0 | `CONDITIONAL_JUMP`
<a id="insn-00badb18"></a> `00badb18` | `09 f8 87 52` | mov w9,#0x3fc0 | `FALL_THROUGH`
<a id="insn-00badb1c"></a> `00badb1c` | `0a 1b 80 52` | mov w10,#0xd8 | `FALL_THROUGH`
<a id="insn-00badb20"></a> `00badb20` | `04 00 00 14` | b 0x00badb30 | `UNCONDITIONAL_JUMP`
<a id="insn-00badb24"></a> `00badb24` | `42 10 00 91` | add x2,x2,#0x4 | `FALL_THROUGH`
<a id="insn-00badb28"></a> `00badb28` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badb2c"></a> `00badb2c` | `a2 03 00 54` | b.cs 0x00badba0 | `CONDITIONAL_JUMP`
<a id="insn-00badb30"></a> `00badb30` | `4b 00 40 b9` | ldr w11,[x2] | `FALL_THROUGH`
<a id="insn-00badb34"></a> `00badb34` | `6c 7d 0b 53` | lsr w12,w11,#0xb | `FALL_THROUGH`
<a id="insn-00badb38"></a> `00badb38` | `9f 6d 00 71` | cmp w12,#0x1b | `FALL_THROUGH`
<a id="insn-00badb3c"></a> `00badb3c` | `00 11 4b fa` | ccmp x8,x11,#0x0,ne | `FALL_THROUGH`
<a id="insn-00badb40"></a> `00badb40` | `43 03 00 54` | b.cc 0x00badba8 | `CONDITIONAL_JUMP`
<a id="insn-00badb44"></a> `00badb44` | `6d 7d 10 53` | lsr w13,w11,#0x10 | `FALL_THROUGH`
<a id="insn-00badb48"></a> `00badb48` | `cc 00 05 cb` | sub x12,x6,x5 | `FALL_THROUGH`
<a id="insn-00badb4c"></a> `00badb4c` | `ad 00 00 35` | cbnz w13,0x00badb60 | `CONDITIONAL_JUMP`
<a id="insn-00badb50"></a> `00badb50` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00badb54"></a> `00badb54` | `6b fd ff 54` | b.lt 0x00badb00 | `CONDITIONAL_JUMP`
<a id="insn-00badb58"></a> `00badb58` | `ab 24 00 78` | strh w11,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00badb5c"></a> `00badb5c` | `f2 ff ff 17` | b 0x00badb24 | `UNCONDITIONAL_JUMP`
<a id="insn-00badb60"></a> `00badb60` | `9f 11 00 f1` | cmp x12,#0x4 | `FALL_THROUGH`
<a id="insn-00badb64"></a> `00badb64` | `eb fc ff 54` | b.lt 0x00badb00 | `CONDITIONAL_JUMP`
<a id="insn-00badb68"></a> `00badb68` | `6c 7d 0a 53` | lsr w12,w11,#0xa | `FALL_THROUGH`
<a id="insn-00badb6c"></a> `00badb6c` | `8e 1b 80 52` | mov w14,#0xdc | `FALL_THROUGH`
<a id="insn-00badb70"></a> `00badb70` | `ab 08 00 39` | strb w11,[x5, #0x2] | `FALL_THROUGH`
<a id="insn-00badb74"></a> `00badb74` | `6e 25 08 33` | bfxil w14,w11,#0x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badb78"></a> `00badb78` | `8c 11 1a 12` | and w12,w12,#0x7c0 | `FALL_THROUGH`
<a id="insn-00badb7c"></a> `00badb7c` | `8c 01 09 0b` | add w12,w12,w9 | `FALL_THROUGH`
<a id="insn-00badb80"></a> `00badb80` | `ae 0c 00 39` | strb w14,[x5, #0x3] | `FALL_THROUGH`
<a id="insn-00badb84"></a> `00badb84` | `4d 21 4c 2a` | orr w13,w10,w12, LSR #0x8 | `FALL_THROUGH`
<a id="insn-00badb88"></a> `00badb88` | `6c 3d 0a 33` | bfxil w12,w11,#0xa,#0x6 | `FALL_THROUGH`
<a id="insn-00badb8c"></a> `00badb8c` | `ab 10 00 91` | add x11,x5,#0x4 | `FALL_THROUGH`
<a id="insn-00badb90"></a> `00badb90` | `ac 00 00 39` | strb w12,[x5] | `FALL_THROUGH`
<a id="insn-00badb94"></a> `00badb94` | `ad 04 00 39` | strb w13,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00badb98"></a> `00badb98` | `e5 03 0b aa` | mov x5,x11 | `FALL_THROUGH`
<a id="insn-00badb9c"></a> `00badb9c` | `e2 ff ff 17` | b 0x00badb24 | `UNCONDITIONAL_JUMP`
<a id="insn-00badba0"></a> `00badba0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00badba4"></a> `00badba4` | `02 00 00 14` | b 0x00badbac | `UNCONDITIONAL_JUMP`
<a id="insn-00badba8"></a> `00badba8` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badbac"></a> `00badbac` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badbb0"></a> `00badbb0` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badbb4"></a> `00badbb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00badae4`](#insn-00badae4) 範囲 `[['00badae4', '00badaf3']]`
  - `CONDITIONAL_JUMP` [`00badaf0`](#insn-00badaf0) → [`00badb10`](#insn-00badb10)
  - `FALL_THROUGH` [`00badaf0`](#insn-00badaf0) → [`00badaf4`](#insn-00badaf4)
- ブロック [`00badaf4`](#insn-00badaf4) 範囲 `[['00badaf4', '00badaff']]`
  - `CONDITIONAL_JUMP` [`00badafc`](#insn-00badafc) → [`00badb08`](#insn-00badb08)
  - `FALL_THROUGH` [`00badafc`](#insn-00badafc) → [`00badb00`](#insn-00badb00)
- ブロック [`00badb00`](#insn-00badb00) 範囲 `[['00badb00', '00badb07']]`
  - `UNCONDITIONAL_JUMP` [`00badb04`](#insn-00badb04) → [`00badbac`](#insn-00badbac)
- ブロック [`00badb08`](#insn-00badb08) 範囲 `[['00badb08', '00badb0f']]`
  - `FALL_THROUGH` [`00badb0c`](#insn-00badb0c) → [`00badb10`](#insn-00badb10)
- ブロック [`00badb10`](#insn-00badb10) 範囲 `[['00badb10', '00badb17']]`
  - `CONDITIONAL_JUMP` [`00badb14`](#insn-00badb14) → [`00badba0`](#insn-00badba0)
  - `FALL_THROUGH` [`00badb14`](#insn-00badb14) → [`00badb18`](#insn-00badb18)
- ブロック [`00badb18`](#insn-00badb18) 範囲 `[['00badb18', '00badb23']]`
  - `UNCONDITIONAL_JUMP` [`00badb20`](#insn-00badb20) → [`00badb30`](#insn-00badb30)
- ブロック [`00badb24`](#insn-00badb24) 範囲 `[['00badb24', '00badb2f']]`
  - `CONDITIONAL_JUMP` [`00badb2c`](#insn-00badb2c) → [`00badba0`](#insn-00badba0)
  - `FALL_THROUGH` [`00badb2c`](#insn-00badb2c) → [`00badb30`](#insn-00badb30)
- ブロック [`00badb30`](#insn-00badb30) 範囲 `[['00badb30', '00badb43']]`
  - `CONDITIONAL_JUMP` [`00badb40`](#insn-00badb40) → [`00badba8`](#insn-00badba8)
  - `FALL_THROUGH` [`00badb40`](#insn-00badb40) → [`00badb44`](#insn-00badb44)
- ブロック [`00badb44`](#insn-00badb44) 範囲 `[['00badb44', '00badb4f']]`
  - `CONDITIONAL_JUMP` [`00badb4c`](#insn-00badb4c) → [`00badb60`](#insn-00badb60)
  - `FALL_THROUGH` [`00badb4c`](#insn-00badb4c) → [`00badb50`](#insn-00badb50)
- ブロック [`00badb50`](#insn-00badb50) 範囲 `[['00badb50', '00badb57']]`
  - `CONDITIONAL_JUMP` [`00badb54`](#insn-00badb54) → [`00badb00`](#insn-00badb00)
  - `FALL_THROUGH` [`00badb54`](#insn-00badb54) → [`00badb58`](#insn-00badb58)
- ブロック [`00badb58`](#insn-00badb58) 範囲 `[['00badb58', '00badb5f']]`
  - `UNCONDITIONAL_JUMP` [`00badb5c`](#insn-00badb5c) → [`00badb24`](#insn-00badb24)
- ブロック [`00badb60`](#insn-00badb60) 範囲 `[['00badb60', '00badb67']]`
  - `CONDITIONAL_JUMP` [`00badb64`](#insn-00badb64) → [`00badb00`](#insn-00badb00)
  - `FALL_THROUGH` [`00badb64`](#insn-00badb64) → [`00badb68`](#insn-00badb68)
- ブロック [`00badb68`](#insn-00badb68) 範囲 `[['00badb68', '00badb9f']]`
  - `UNCONDITIONAL_JUMP` [`00badb9c`](#insn-00badb9c) → [`00badb24`](#insn-00badb24)
- ブロック [`00badba0`](#insn-00badba0) 範囲 `[['00badba0', '00badba7']]`
  - `UNCONDITIONAL_JUMP` [`00badba4`](#insn-00badba4) → [`00badbac`](#insn-00badbac)
- ブロック [`00badba8`](#insn-00badba8) 範囲 `[['00badba8', '00badbab']]`
  - `FALL_THROUGH` [`00badba8`](#insn-00badba8) → [`00badbac`](#insn-00badbac)
- ブロック [`00badbac`](#insn-00badbac) 範囲 `[['00badbac', '00badbb7']]`

## 命令位置別の参照

- [`00badaf0`](#insn-00badaf0) → [`00badb10`](#insn-00badb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badafc`](#insn-00badafc) → [`00badb08`](#insn-00badb08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb04`](#insn-00badb04) → [`00badbac`](#insn-00badbac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb14`](#insn-00badb14) → [`00badba0`](#insn-00badba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb20`](#insn-00badb20) → [`00badb30`](#insn-00badb30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb2c`](#insn-00badb2c) → [`00badba0`](#insn-00badba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb40`](#insn-00badb40) → [`00badba8`](#insn-00badba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb4c`](#insn-00badb4c) → [`00badb60`](#insn-00badb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb54`](#insn-00badb54) → [`00badb00`](#insn-00badb00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb5c`](#insn-00badb5c) → [`00badb24`](#insn-00badb24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb64`](#insn-00badb64) → [`00badb00`](#insn-00badb00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badb9c`](#insn-00badb9c) → [`00badb24`](#insn-00badb24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badba4`](#insn-00badba4) → [`00badbac`](#insn-00badbac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badaf0`](#insn-00badaf0)

~~~json
{
  "source": "00badaf0",
  "target": "00badb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badafc`](#insn-00badafc)

~~~json
{
  "source": "00badafc",
  "target": "00badb08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb04`](#insn-00badb04)

~~~json
{
  "source": "00badb04",
  "target": "00badbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb14`](#insn-00badb14)

~~~json
{
  "source": "00badb14",
  "target": "00badba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb20`](#insn-00badb20)

~~~json
{
  "source": "00badb20",
  "target": "00badb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb2c`](#insn-00badb2c)

~~~json
{
  "source": "00badb2c",
  "target": "00badba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb40`](#insn-00badb40)

~~~json
{
  "source": "00badb40",
  "target": "00badba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb4c`](#insn-00badb4c)

~~~json
{
  "source": "00badb4c",
  "target": "00badb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb54`](#insn-00badb54)

~~~json
{
  "source": "00badb54",
  "target": "00badb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb5c`](#insn-00badb5c)

~~~json
{
  "source": "00badb5c",
  "target": "00badb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb64`](#insn-00badb64)

~~~json
{
  "source": "00badb64",
  "target": "00badb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badb9c`](#insn-00badb9c)

~~~json
{
  "source": "00badb9c",
  "target": "00badb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badba4`](#insn-00badba4)

~~~json
{
  "source": "00badba4",
  "target": "00badbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
