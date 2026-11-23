# 00bade9c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baddd4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00baddd4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-e9e7e251112601a8bdddac4874ef4fb9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00badee0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badee0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-a9a87bcd08e53bad9a5efb803d71d6fc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bade9c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3689d07aa554c5c1c102820e750eee834a55b55ae5b2b5052a0d2fe0a9d71324",
  "source_text_sha256": "3689d07aa554c5c1c102820e750eee834a55b55ae5b2b5052a0d2fe0a9d71324",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bade9c",
        "00badf2f"
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
      goto LAB_00badf24;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00badf24:
  *param_5 = (ulong)param_3;
  *param_8 = param_6;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bade9c"></a> `00bade9c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badea0"></a> `00badea0` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badea4"></a> `00badea4` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badea8"></a> `00badea8` | `4b 01 00 54` | b.lt 0x00baded0 | `CONDITIONAL_JUMP`
<a id="insn-00badeac"></a> `00badeac` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badeb0"></a> `00badeb0` | `08 01 10 36` | tbz w8,#0x2,0x00baded0 | `CONDITIONAL_JUMP`
<a id="insn-00badeb4"></a> `00badeb4` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badeb8"></a> `00badeb8` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badebc"></a> `00badebc` | `a1 00 00 54` | b.ne 0x00baded0 | `CONDITIONAL_JUMP`
<a id="insn-00badec0"></a> `00badec0` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badec4"></a> `00badec4` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badec8"></a> `00badec8` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badecc"></a> `00badecc` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00baded0"></a> `00baded0` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00baded4"></a> `00baded4` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00baded8"></a> `00baded8` | `22 02 00 54` | b.cs 0x00badf1c | `CONDITIONAL_JUMP`
<a id="insn-00badedc"></a> `00badedc` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00badee0"></a> `00badee0` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badee4"></a> `00badee4` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00badee8"></a> `00badee8` | `a2 01 00 54` | b.cs 0x00badf1c | `CONDITIONAL_JUMP`
<a id="insn-00badeec"></a> `00badeec` | `4a 00 40 39` | ldrb w10,[x2] | `FALL_THROUGH`
<a id="insn-00badef0"></a> `00badef0` | `4b 11 1d 12` | and w11,w10,#0xf8 | `FALL_THROUGH`
<a id="insn-00badef4"></a> `00badef4` | `7f 61 03 71` | cmp w11,#0xd8 | `FALL_THROUGH`
<a id="insn-00badef8"></a> `00badef8` | `60 01 00 54` | b.eq 0x00badf24 | `CONDITIONAL_JUMP`
<a id="insn-00badefc"></a> `00badefc` | `4b 04 40 39` | ldrb w11,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badf00"></a> `00badf00` | `6a 21 0a 2a` | orr w10,w11,w10, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00badf04"></a> `00badf04` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00badf08"></a> `00badf08` | `e3 00 00 54` | b.cc 0x00badf24 | `CONDITIONAL_JUMP`
<a id="insn-00badf0c"></a> `00badf0c` | `42 08 00 91` | add x2,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00badf10"></a> `00badf10` | `aa 24 00 78` | strh w10,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00badf14"></a> `00badf14` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badf18"></a> `00badf18` | `63 fe ff 54` | b.cc 0x00badee4 | `CONDITIONAL_JUMP`
<a id="insn-00badf1c"></a> `00badf1c` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badf20"></a> `00badf20` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00badf24"></a> `00badf24` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badf28"></a> `00badf28` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badf2c"></a> `00badf2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bade9c`](#insn-00bade9c) 範囲 `[['00bade9c', '00badeab']]`
  - `CONDITIONAL_JUMP` [`00badea8`](#insn-00badea8) → [`00baded0`](#insn-00baded0)
  - `FALL_THROUGH` [`00badea8`](#insn-00badea8) → [`00badeac`](#insn-00badeac)
- ブロック [`00badeac`](#insn-00badeac) 範囲 `[['00badeac', '00badeb3']]`
  - `CONDITIONAL_JUMP` [`00badeb0`](#insn-00badeb0) → [`00baded0`](#insn-00baded0)
  - `FALL_THROUGH` [`00badeb0`](#insn-00badeb0) → [`00badeb4`](#insn-00badeb4)
- ブロック [`00badeb4`](#insn-00badeb4) 範囲 `[['00badeb4', '00badebf']]`
  - `CONDITIONAL_JUMP` [`00badebc`](#insn-00badebc) → [`00baded0`](#insn-00baded0)
  - `FALL_THROUGH` [`00badebc`](#insn-00badebc) → [`00badec0`](#insn-00badec0)
- ブロック [`00badec0`](#insn-00badec0) 範囲 `[['00badec0', '00badecf']]`
  - `FALL_THROUGH` [`00badecc`](#insn-00badecc) → [`00baded0`](#insn-00baded0)
- ブロック [`00baded0`](#insn-00baded0) 範囲 `[['00baded0', '00badedb']]`
  - `CONDITIONAL_JUMP` [`00baded8`](#insn-00baded8) → [`00badf1c`](#insn-00badf1c)
  - `FALL_THROUGH` [`00baded8`](#insn-00baded8) → [`00badedc`](#insn-00badedc)
- ブロック [`00badedc`](#insn-00badedc) 範囲 `[['00badedc', '00badee3']]`
  - `FALL_THROUGH` [`00badee0`](#insn-00badee0) → [`00badee4`](#insn-00badee4)
- ブロック [`00badee4`](#insn-00badee4) 範囲 `[['00badee4', '00badeeb']]`
  - `CONDITIONAL_JUMP` [`00badee8`](#insn-00badee8) → [`00badf1c`](#insn-00badf1c)
  - `FALL_THROUGH` [`00badee8`](#insn-00badee8) → [`00badeec`](#insn-00badeec)
- ブロック [`00badeec`](#insn-00badeec) 範囲 `[['00badeec', '00badefb']]`
  - `CONDITIONAL_JUMP` [`00badef8`](#insn-00badef8) → [`00badf24`](#insn-00badf24)
  - `FALL_THROUGH` [`00badef8`](#insn-00badef8) → [`00badefc`](#insn-00badefc)
- ブロック [`00badefc`](#insn-00badefc) 範囲 `[['00badefc', '00badf0b']]`
  - `CONDITIONAL_JUMP` [`00badf08`](#insn-00badf08) → [`00badf24`](#insn-00badf24)
  - `FALL_THROUGH` [`00badf08`](#insn-00badf08) → [`00badf0c`](#insn-00badf0c)
- ブロック [`00badf0c`](#insn-00badf0c) 範囲 `[['00badf0c', '00badf1b']]`
  - `CONDITIONAL_JUMP` [`00badf18`](#insn-00badf18) → [`00badee4`](#insn-00badee4)
  - `FALL_THROUGH` [`00badf18`](#insn-00badf18) → [`00badf1c`](#insn-00badf1c)
- ブロック [`00badf1c`](#insn-00badf1c) 範囲 `[['00badf1c', '00badf23']]`
  - `FALL_THROUGH` [`00badf20`](#insn-00badf20) → [`00badf24`](#insn-00badf24)
- ブロック [`00badf24`](#insn-00badf24) 範囲 `[['00badf24', '00badf2f']]`

## 命令位置別の参照

- [`00badea8`](#insn-00badea8) → [`00baded0`](#insn-00baded0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badeb0`](#insn-00badeb0) → [`00baded0`](#insn-00baded0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badebc`](#insn-00badebc) → [`00baded0`](#insn-00baded0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baded8`](#insn-00baded8) → [`00badf1c`](#insn-00badf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badee8`](#insn-00badee8) → [`00badf1c`](#insn-00badf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badef8`](#insn-00badef8) → [`00badf24`](#insn-00badf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf08`](#insn-00badf08) → [`00badf24`](#insn-00badf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf18`](#insn-00badf18) → [`00badee4`](#insn-00badee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badea8`](#insn-00badea8)

~~~json
{
  "source": "00badea8",
  "target": "00baded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badeb0`](#insn-00badeb0)

~~~json
{
  "source": "00badeb0",
  "target": "00baded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badebc`](#insn-00badebc)

~~~json
{
  "source": "00badebc",
  "target": "00baded0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baded8`](#insn-00baded8)

~~~json
{
  "source": "00baded8",
  "target": "00badf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badee8`](#insn-00badee8)

~~~json
{
  "source": "00badee8",
  "target": "00badf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badef8`](#insn-00badef8)

~~~json
{
  "source": "00badef8",
  "target": "00badf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf08`](#insn-00badf08)

~~~json
{
  "source": "00badf08",
  "target": "00badf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf18`](#insn-00badf18)

~~~json
{
  "source": "00badf18",
  "target": "00badee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
