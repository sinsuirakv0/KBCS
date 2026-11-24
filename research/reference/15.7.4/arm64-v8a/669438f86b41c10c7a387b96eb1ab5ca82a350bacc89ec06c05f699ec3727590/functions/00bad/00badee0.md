# 00badee0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bade9c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00bade9c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-a9a87bcd08e53bad9a5efb803d71d6fc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2a928`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a928.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-c80bbd1b164a1205d3f1d4409aba9d06)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badee0",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b53ed63dc1b68ec01cc3d772199961cb40b74e1d3ae1426e6d97dd7447295ff1",
  "source_text_sha256": "b53ed63dc1b68ec01cc3d772199961cb40b74e1d3ae1426e6d97dd7447295ff1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badee0",
        "00badf73"
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
      goto LAB_00badf68;
      param_3 = param_3 + 2;
      param_6 = puVar3 + 1;
      *puVar3 = uVar1;
      puVar3 = param_6;
      if (param_4 + -1 <= param_3) break;
    }
  }
  uVar2 = param_3 < param_4;
LAB_00badf68:
  *param_5 = (ulong)param_3;
  *param_8 = param_6;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badee0"></a> `00badee0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badee4"></a> `00badee4` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00badee8"></a> `00badee8` | `1f 09 00 f1` | cmp x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badeec"></a> `00badeec` | `4b 01 00 54` | b.lt 0x00badf14 | `CONDITIONAL_JUMP`
<a id="insn-00badef0"></a> `00badef0` | `08 18 40 b9` | ldr w8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00badef4"></a> `00badef4` | `08 01 10 36` | tbz w8,#0x2,0x00badf14 | `CONDITIONAL_JUMP`
<a id="insn-00badef8"></a> `00badef8` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00badefc"></a> `00badefc` | `1f f9 03 71` | cmp w8,#0xfe | `FALL_THROUGH`
<a id="insn-00badf00"></a> `00badf00` | `a1 00 00 54` | b.ne 0x00badf14 | `CONDITIONAL_JUMP`
<a id="insn-00badf04"></a> `00badf04` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badf08"></a> `00badf08` | `1f fd 03 71` | cmp w8,#0xff | `FALL_THROUGH`
<a id="insn-00badf0c"></a> `00badf0c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00badf10"></a> `00badf10` | `42 44 28 8b` | add x2,x2,w8, UXTW  #0x1 | `FALL_THROUGH`
<a id="insn-00badf14"></a> `00badf14` | `68 04 00 d1` | sub x8,x3,#0x1 | `FALL_THROUGH`
<a id="insn-00badf18"></a> `00badf18` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badf1c"></a> `00badf1c` | `22 02 00 54` | b.cs 0x00badf60 | `CONDITIONAL_JUMP`
<a id="insn-00badf20"></a> `00badf20` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00badf24"></a> `00badf24` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badf28"></a> `00badf28` | `bf 00 06 eb` | cmp x5,x6 | `FALL_THROUGH`
<a id="insn-00badf2c"></a> `00badf2c` | `a2 01 00 54` | b.cs 0x00badf60 | `CONDITIONAL_JUMP`
<a id="insn-00badf30"></a> `00badf30` | `4a 00 40 39` | ldrb w10,[x2] | `FALL_THROUGH`
<a id="insn-00badf34"></a> `00badf34` | `4b 11 1d 12` | and w11,w10,#0xf8 | `FALL_THROUGH`
<a id="insn-00badf38"></a> `00badf38` | `7f 61 03 71` | cmp w11,#0xd8 | `FALL_THROUGH`
<a id="insn-00badf3c"></a> `00badf3c` | `60 01 00 54` | b.eq 0x00badf68 | `CONDITIONAL_JUMP`
<a id="insn-00badf40"></a> `00badf40` | `4b 04 40 39` | ldrb w11,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00badf44"></a> `00badf44` | `6a 21 0a 2a` | orr w10,w11,w10, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00badf48"></a> `00badf48` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00badf4c"></a> `00badf4c` | `e3 00 00 54` | b.cc 0x00badf68 | `CONDITIONAL_JUMP`
<a id="insn-00badf50"></a> `00badf50` | `42 08 00 91` | add x2,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00badf54"></a> `00badf54` | `aa 24 00 78` | strh w10,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00badf58"></a> `00badf58` | `5f 00 08 eb` | cmp x2,x8 | `FALL_THROUGH`
<a id="insn-00badf5c"></a> `00badf5c` | `63 fe ff 54` | b.cc 0x00badf28 | `CONDITIONAL_JUMP`
<a id="insn-00badf60"></a> `00badf60` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00badf64"></a> `00badf64` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-00badf68"></a> `00badf68` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badf6c"></a> `00badf6c` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badf70"></a> `00badf70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00badee0`](#insn-00badee0) 範囲 `[['00badee0', '00badeef']]`
  - `CONDITIONAL_JUMP` [`00badeec`](#insn-00badeec) → [`00badf14`](#insn-00badf14)
  - `FALL_THROUGH` [`00badeec`](#insn-00badeec) → [`00badef0`](#insn-00badef0)
- ブロック [`00badef0`](#insn-00badef0) 範囲 `[['00badef0', '00badef7']]`
  - `CONDITIONAL_JUMP` [`00badef4`](#insn-00badef4) → [`00badf14`](#insn-00badf14)
  - `FALL_THROUGH` [`00badef4`](#insn-00badef4) → [`00badef8`](#insn-00badef8)
- ブロック [`00badef8`](#insn-00badef8) 範囲 `[['00badef8', '00badf03']]`
  - `CONDITIONAL_JUMP` [`00badf00`](#insn-00badf00) → [`00badf14`](#insn-00badf14)
  - `FALL_THROUGH` [`00badf00`](#insn-00badf00) → [`00badf04`](#insn-00badf04)
- ブロック [`00badf04`](#insn-00badf04) 範囲 `[['00badf04', '00badf13']]`
  - `FALL_THROUGH` [`00badf10`](#insn-00badf10) → [`00badf14`](#insn-00badf14)
- ブロック [`00badf14`](#insn-00badf14) 範囲 `[['00badf14', '00badf1f']]`
  - `CONDITIONAL_JUMP` [`00badf1c`](#insn-00badf1c) → [`00badf60`](#insn-00badf60)
  - `FALL_THROUGH` [`00badf1c`](#insn-00badf1c) → [`00badf20`](#insn-00badf20)
- ブロック [`00badf20`](#insn-00badf20) 範囲 `[['00badf20', '00badf27']]`
  - `FALL_THROUGH` [`00badf24`](#insn-00badf24) → [`00badf28`](#insn-00badf28)
- ブロック [`00badf28`](#insn-00badf28) 範囲 `[['00badf28', '00badf2f']]`
  - `CONDITIONAL_JUMP` [`00badf2c`](#insn-00badf2c) → [`00badf60`](#insn-00badf60)
  - `FALL_THROUGH` [`00badf2c`](#insn-00badf2c) → [`00badf30`](#insn-00badf30)
- ブロック [`00badf30`](#insn-00badf30) 範囲 `[['00badf30', '00badf3f']]`
  - `CONDITIONAL_JUMP` [`00badf3c`](#insn-00badf3c) → [`00badf68`](#insn-00badf68)
  - `FALL_THROUGH` [`00badf3c`](#insn-00badf3c) → [`00badf40`](#insn-00badf40)
- ブロック [`00badf40`](#insn-00badf40) 範囲 `[['00badf40', '00badf4f']]`
  - `CONDITIONAL_JUMP` [`00badf4c`](#insn-00badf4c) → [`00badf68`](#insn-00badf68)
  - `FALL_THROUGH` [`00badf4c`](#insn-00badf4c) → [`00badf50`](#insn-00badf50)
- ブロック [`00badf50`](#insn-00badf50) 範囲 `[['00badf50', '00badf5f']]`
  - `CONDITIONAL_JUMP` [`00badf5c`](#insn-00badf5c) → [`00badf28`](#insn-00badf28)
  - `FALL_THROUGH` [`00badf5c`](#insn-00badf5c) → [`00badf60`](#insn-00badf60)
- ブロック [`00badf60`](#insn-00badf60) 範囲 `[['00badf60', '00badf67']]`
  - `FALL_THROUGH` [`00badf64`](#insn-00badf64) → [`00badf68`](#insn-00badf68)
- ブロック [`00badf68`](#insn-00badf68) 範囲 `[['00badf68', '00badf73']]`

## 命令位置別の参照

- [`00badeec`](#insn-00badeec) → [`00badf14`](#insn-00badf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badef4`](#insn-00badef4) → [`00badf14`](#insn-00badf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf00`](#insn-00badf00) → [`00badf14`](#insn-00badf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf1c`](#insn-00badf1c) → [`00badf60`](#insn-00badf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf2c`](#insn-00badf2c) → [`00badf60`](#insn-00badf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf3c`](#insn-00badf3c) → [`00badf68`](#insn-00badf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf4c`](#insn-00badf4c) → [`00badf68`](#insn-00badf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badf5c`](#insn-00badf5c) → [`00badf28`](#insn-00badf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00badeec`](#insn-00badeec)

~~~json
{
  "source": "00badeec",
  "target": "00badf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badef4`](#insn-00badef4)

~~~json
{
  "source": "00badef4",
  "target": "00badf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf00`](#insn-00badf00)

~~~json
{
  "source": "00badf00",
  "target": "00badf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf1c`](#insn-00badf1c)

~~~json
{
  "source": "00badf1c",
  "target": "00badf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf2c`](#insn-00badf2c)

~~~json
{
  "source": "00badf2c",
  "target": "00badf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf3c`](#insn-00badf3c)

~~~json
{
  "source": "00badf3c",
  "target": "00badf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf4c`](#insn-00badf4c)

~~~json
{
  "source": "00badf4c",
  "target": "00badf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badf5c`](#insn-00badf5c)

~~~json
{
  "source": "00badf5c",
  "target": "00badf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
