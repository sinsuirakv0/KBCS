# 00baddd4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bade9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bade9c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-e9e7e251112601a8bdddac4874ef4fb9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baddd4",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "796a119fded983f463e512530f3bf7968fc7e79e595e5b6d61b3fb1c64d8ea68",
  "source_text_sha256": "796a119fded983f463e512530f3bf7968fc7e79e595e5b6d61b3fb1c64d8ea68",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baddd4",
        "00bade67"
      ]
    ],
    "bytes_sha256": "b3a7ca12fc2fe93be1a2845088b697c23a965f353ad87eeaf08c86309dd99fe1",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
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

## 疑似コード / UTF-8 1045 bytes

~~~c

undefined1
_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_
          (long param_1,undefined8 param_2,byte *param_3,byte *param_4,ulong *param_5,
          ushort *param_6,ushort *param_7,undefined8 *param_8)

{
  ushort uVar1;
  undefined1 uVar2;
  ushort *puVar3;
  ulong uVar4;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == 0xfe)) {
    param_3 = param_3 + (ulong)(param_3[1] == 0xff) * 2;
  }
  if (param_3 < param_4 + -1) {
    uVar4 = *(ulong *)(param_1 + 0x10);
    uVar2 = 2;
    puVar3 = param_6;
    while (param_6 = puVar3, puVar3 < param_7) {
      if (((*param_3 & 0xf8) == 0xd8) || (uVar1 = CONCAT11(*param_3,param_3[1]), uVar4 < uVar1))
      goto LAB_00bade5c;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00bade5c:
  *param_5 = (ulong)param_3;
  *param_8 = param_6;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baddd4"></a> `00baddd4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baddd8"></a> `00baddd8` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badddc"></a> `00badddc` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badde0"></a> `00badde0` | `4b 01 00 54` | b.lt 0x00bade08 | `CONDITIONAL_JUMP`
<a id="insn-00badde4"></a> `00badde4` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badde8"></a> `00badde8` | `08 01 10 36` | tbz w8,#0x2,0x00bade08 | `CONDITIONAL_JUMP`
<a id="insn-00baddec"></a> `00baddec` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00baddf0"></a> `00baddf0` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00baddf4"></a> `00baddf4` | `a1 00 00 54` | b.ne 0x00bade08 | `CONDITIONAL_JUMP`
<a id="insn-00baddf8"></a> `00baddf8` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00baddfc"></a> `00baddfc` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00bade00"></a> `00bade00` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bade04"></a> `00bade04` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00bade08"></a> `00bade08` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00bade0c"></a> `00bade0c` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00bade10"></a> `00bade10` | `22 02 00 54` | b.cs 0x00bade54 | `CONDITIONAL_JUMP`
<a id="insn-00bade14"></a> `00bade14` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bade18"></a> `00bade18` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bade1c"></a> `00bade1c` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00bade20"></a> `00bade20` | `a2 01 00 54` | b.cs 0x00bade54 | `CONDITIONAL_JUMP`
<a id="insn-00bade24"></a> `00bade24` | `4a 00 40 39` | ldrb w10,[x2] | `FALL_THROUGH`
<a id="insn-00bade28"></a> `00bade28` | `4b 11 1d 12` | and w11,w10,#0xf8 | `FALL_THROUGH`
<a id="insn-00bade2c"></a> `00bade2c` | `7f 61 03 71` | cmp w11,#0xd8 | `FALL_THROUGH`
<a id="insn-00bade30"></a> `00bade30` | `60 01 00 54` | b.eq 0x00bade5c | `CONDITIONAL_JUMP`
<a id="insn-00bade34"></a> `00bade34` | `4b 04 40 39` | ldrb w11,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00bade38"></a> `00bade38` | `6a 21 0a 2a` | orr w10,w11,w10, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00bade3c"></a> `00bade3c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bade40"></a> `00bade40` | `e3 00 00 54` | b.cc 0x00bade5c | `CONDITIONAL_JUMP`
<a id="insn-00bade44"></a> `00bade44` | `42 08 00 91` | add x2,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00bade48"></a> `00bade48` | `aa 24 00 78` | strh w10,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00bade4c"></a> `00bade4c` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00bade50"></a> `00bade50` | `63 fe ff 54` | b.cc 0x00bade1c | `CONDITIONAL_JUMP`
<a id="insn-00bade54"></a> `00bade54` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bade58"></a> `00bade58` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00bade5c"></a> `00bade5c` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00bade60"></a> `00bade60` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00bade64"></a> `00bade64` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baddd4`](#insn-00baddd4) 範囲 `[['00baddd4', '00badde3']]`
  - `CONDITIONAL_JUMP` [`00badde0`](#insn-00badde0) → [`00bade08`](#insn-00bade08)
  - `FALL_THROUGH` [`00badde0`](#insn-00badde0) → [`00badde4`](#insn-00badde4)
- ブロック [`00badde4`](#insn-00badde4) 範囲 `[['00badde4', '00baddeb']]`
  - `CONDITIONAL_JUMP` [`00badde8`](#insn-00badde8) → [`00bade08`](#insn-00bade08)
  - `FALL_THROUGH` [`00badde8`](#insn-00badde8) → [`00baddec`](#insn-00baddec)
- ブロック [`00baddec`](#insn-00baddec) 範囲 `[['00baddec', '00baddf7']]`
  - `CONDITIONAL_JUMP` [`00baddf4`](#insn-00baddf4) → [`00bade08`](#insn-00bade08)
  - `FALL_THROUGH` [`00baddf4`](#insn-00baddf4) → [`00baddf8`](#insn-00baddf8)
- ブロック [`00baddf8`](#insn-00baddf8) 範囲 `[['00baddf8', '00bade07']]`
  - `FALL_THROUGH` [`00bade04`](#insn-00bade04) → [`00bade08`](#insn-00bade08)
- ブロック [`00bade08`](#insn-00bade08) 範囲 `[['00bade08', '00bade13']]`
  - `CONDITIONAL_JUMP` [`00bade10`](#insn-00bade10) → [`00bade54`](#insn-00bade54)
  - `FALL_THROUGH` [`00bade10`](#insn-00bade10) → [`00bade14`](#insn-00bade14)
- ブロック [`00bade14`](#insn-00bade14) 範囲 `[['00bade14', '00bade1b']]`
  - `FALL_THROUGH` [`00bade18`](#insn-00bade18) → [`00bade1c`](#insn-00bade1c)
- ブロック [`00bade1c`](#insn-00bade1c) 範囲 `[['00bade1c', '00bade23']]`
  - `CONDITIONAL_JUMP` [`00bade20`](#insn-00bade20) → [`00bade54`](#insn-00bade54)
  - `FALL_THROUGH` [`00bade20`](#insn-00bade20) → [`00bade24`](#insn-00bade24)
- ブロック [`00bade24`](#insn-00bade24) 範囲 `[['00bade24', '00bade33']]`
  - `CONDITIONAL_JUMP` [`00bade30`](#insn-00bade30) → [`00bade5c`](#insn-00bade5c)
  - `FALL_THROUGH` [`00bade30`](#insn-00bade30) → [`00bade34`](#insn-00bade34)
- ブロック [`00bade34`](#insn-00bade34) 範囲 `[['00bade34', '00bade43']]`
  - `CONDITIONAL_JUMP` [`00bade40`](#insn-00bade40) → [`00bade5c`](#insn-00bade5c)
  - `FALL_THROUGH` [`00bade40`](#insn-00bade40) → [`00bade44`](#insn-00bade44)
- ブロック [`00bade44`](#insn-00bade44) 範囲 `[['00bade44', '00bade53']]`
  - `CONDITIONAL_JUMP` [`00bade50`](#insn-00bade50) → [`00bade1c`](#insn-00bade1c)
  - `FALL_THROUGH` [`00bade50`](#insn-00bade50) → [`00bade54`](#insn-00bade54)
- ブロック [`00bade54`](#insn-00bade54) 範囲 `[['00bade54', '00bade5b']]`
  - `FALL_THROUGH` [`00bade58`](#insn-00bade58) → [`00bade5c`](#insn-00bade5c)
- ブロック [`00bade5c`](#insn-00bade5c) 範囲 `[['00bade5c', '00bade67']]`

## 命令位置別の参照

- [`00badde0`](#insn-00badde0) → [`00bade08`](#insn-00bade08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badde8`](#insn-00badde8) → [`00bade08`](#insn-00bade08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baddf4`](#insn-00baddf4) → [`00bade08`](#insn-00bade08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade10`](#insn-00bade10) → [`00bade54`](#insn-00bade54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade20`](#insn-00bade20) → [`00bade54`](#insn-00bade54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade30`](#insn-00bade30) → [`00bade5c`](#insn-00bade5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade40`](#insn-00bade40) → [`00bade5c`](#insn-00bade5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bade50`](#insn-00bade50) → [`00bade1c`](#insn-00bade1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badde0`](#insn-00badde0)

~~~json
{
  "source": "00badde0",
  "target": "00bade08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badde8`](#insn-00badde8)

~~~json
{
  "source": "00badde8",
  "target": "00bade08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baddf4`](#insn-00baddf4)

~~~json
{
  "source": "00baddf4",
  "target": "00bade08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade10`](#insn-00bade10)

~~~json
{
  "source": "00bade10",
  "target": "00bade54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade20`](#insn-00bade20)

~~~json
{
  "source": "00bade20",
  "target": "00bade54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade30`](#insn-00bade30)

~~~json
{
  "source": "00bade30",
  "target": "00bade5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade40`](#insn-00bade40)

~~~json
{
  "source": "00bade40",
  "target": "00bade5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bade50`](#insn-00bade50)

~~~json
{
  "source": "00bade50",
  "target": "00bade1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
