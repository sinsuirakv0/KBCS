# 00bfbda0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbd04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-47be016882b36d68a0ecee7aed54f7cb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfcd94`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcd94.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-73e7e2afa4e92a4181ec0a119faa6062)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbda0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bdc166147001eed9a20f9ac35b4d392885538b25e366131393c3a8bd8c799fc0",
  "source_text_sha256": "bdc166147001eed9a20f9ac35b4d392885538b25e366131393c3a8bd8c799fc0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbda0",
        "00bfbe23"
      ]
    ],
    "bytes_sha256": "0814b993bf392c0570fe6d76a5105d814643dec241838e640f6efc9d58b4701f",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 764 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv(long *param_1)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((byte *)param_1[3] == (byte *)param_1[4]) {
    uVar1 = (**(code **)(*param_1 + 0x50))();
    if ((int)uVar1 == -1) {
      return uVar1;
    }
    pbVar2 = (byte *)param_1[3];
    if (pbVar2 == (byte *)param_1[4]) goto LAB_00bfbdfc;
  }
  else {
    pbVar2 = (byte *)param_1[3] + 1;
    param_1[3] = (long)pbVar2;
    if (pbVar2 == (byte *)param_1[4]) {
LAB_00bfbdfc:
                    /* WARNING: Could not recover jumptable at 0x00bfbe10. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      uVar1 = (**(code **)(*param_1 + 0x48))();
      return uVar1;
    }
  }
  return (ulong)*pbVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbda0"></a> `00bfbda0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbda4"></a> `00bfbda4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbda8"></a> `00bfbda8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbdac"></a> `00bfbdac` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbdb0"></a> `00bfbdb0` | `09 a0 41 a9` | ldp x9,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbdb4"></a> `00bfbdb4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfbdb8"></a> `00bfbdb8` | `e0 00 00 54` | b.eq 0x00bfbdd4 | `CONDITIONAL_JUMP`
<a id="insn-00bfbdbc"></a> `00bfbdbc` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbdc0"></a> `00bfbdc0` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbdc4"></a> `00bfbdc4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfbdc8"></a> `00bfbdc8` | `a0 01 00 54` | b.eq 0x00bfbdfc | `CONDITIONAL_JUMP`
<a id="insn-00bfbdcc"></a> `00bfbdcc` | `20 01 40 39` | ldrb w0,[x9] | `FALL_THROUGH`
<a id="insn-00bfbdd0"></a> `00bfbdd0` | `11 00 00 14` | b 0x00bfbe14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfbdd4"></a> `00bfbdd4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfbdd8"></a> `00bfbdd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfbddc"></a> `00bfbddc` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfbde0"></a> `00bfbde0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfbde4"></a> `00bfbde4` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbde8"></a> `00bfbde8` | `60 01 00 54` | b.eq 0x00bfbe14 | `CONDITIONAL_JUMP`
<a id="insn-00bfbdec"></a> `00bfbdec` | `69 a2 41 a9` | ldp x9,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbdf0"></a> `00bfbdf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfbdf4"></a> `00bfbdf4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfbdf8"></a> `00bfbdf8` | `a1 fe ff 54` | b.ne 0x00bfbdcc | `CONDITIONAL_JUMP`
<a id="insn-00bfbdfc"></a> `00bfbdfc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfbe00"></a> `00bfbe00` | `10 25 40 f9` | ldr x16,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfbe04"></a> `00bfbe04` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbe08"></a> `00bfbe08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbe0c"></a> `00bfbe0c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbe10"></a> `00bfbe10` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bfbe14"></a> `00bfbe14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbe18"></a> `00bfbe18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfbe1c"></a> `00bfbe1c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbe20"></a> `00bfbe20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbda0`](#insn-00bfbda0) 範囲 `[['00bfbda0', '00bfbdbb']]`
  - `CONDITIONAL_JUMP` [`00bfbdb8`](#insn-00bfbdb8) → [`00bfbdd4`](#insn-00bfbdd4)
  - `FALL_THROUGH` [`00bfbdb8`](#insn-00bfbdb8) → [`00bfbdbc`](#insn-00bfbdbc)
- ブロック [`00bfbdbc`](#insn-00bfbdbc) 範囲 `[['00bfbdbc', '00bfbdcb']]`
  - `CONDITIONAL_JUMP` [`00bfbdc8`](#insn-00bfbdc8) → [`00bfbdfc`](#insn-00bfbdfc)
  - `FALL_THROUGH` [`00bfbdc8`](#insn-00bfbdc8) → [`00bfbdcc`](#insn-00bfbdcc)
- ブロック [`00bfbdcc`](#insn-00bfbdcc) 範囲 `[['00bfbdcc', '00bfbdd3']]`
  - `UNCONDITIONAL_JUMP` [`00bfbdd0`](#insn-00bfbdd0) → [`00bfbe14`](#insn-00bfbe14)
- ブロック [`00bfbdd4`](#insn-00bfbdd4) 範囲 `[['00bfbdd4', '00bfbdeb']]`
  - `CONDITIONAL_JUMP` [`00bfbde8`](#insn-00bfbde8) → [`00bfbe14`](#insn-00bfbe14)
  - `FALL_THROUGH` [`00bfbde8`](#insn-00bfbde8) → [`00bfbdec`](#insn-00bfbdec)
- ブロック [`00bfbdec`](#insn-00bfbdec) 範囲 `[['00bfbdec', '00bfbdfb']]`
  - `CONDITIONAL_JUMP` [`00bfbdf8`](#insn-00bfbdf8) → [`00bfbdcc`](#insn-00bfbdcc)
  - `FALL_THROUGH` [`00bfbdf8`](#insn-00bfbdf8) → [`00bfbdfc`](#insn-00bfbdfc)
- ブロック [`00bfbdfc`](#insn-00bfbdfc) 範囲 `[['00bfbdfc', '00bfbe13']]`
- ブロック [`00bfbe14`](#insn-00bfbe14) 範囲 `[['00bfbe14', '00bfbe23']]`

## 命令位置別の参照

- [`00bfbda4`](#insn-00bfbda4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbda8`](#insn-00bfbda8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdb8`](#insn-00bfbdb8) → [`00bfbdd4`](#insn-00bfbdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdc8`](#insn-00bfbdc8) → [`00bfbdfc`](#insn-00bfbdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdd0`](#insn-00bfbdd0) → [`00bfbe14`](#insn-00bfbe14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbde8`](#insn-00bfbde8) → [`00bfbe14`](#insn-00bfbe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbdf8`](#insn-00bfbdf8) → [`00bfbdcc`](#insn-00bfbdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe04`](#insn-00bfbe04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe08`](#insn-00bfbe08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe14`](#insn-00bfbe14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbe18`](#insn-00bfbe18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbda4`](#insn-00bfbda4)

~~~json
{
  "source": "00bfbda4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbda8`](#insn-00bfbda8)

~~~json
{
  "source": "00bfbda8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdb8`](#insn-00bfbdb8)

~~~json
{
  "source": "00bfbdb8",
  "target": "00bfbdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdc8`](#insn-00bfbdc8)

~~~json
{
  "source": "00bfbdc8",
  "target": "00bfbdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdd0`](#insn-00bfbdd0)

~~~json
{
  "source": "00bfbdd0",
  "target": "00bfbe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbde8`](#insn-00bfbde8)

~~~json
{
  "source": "00bfbde8",
  "target": "00bfbe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbdf8`](#insn-00bfbdf8)

~~~json
{
  "source": "00bfbdf8",
  "target": "00bfbdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe04`](#insn-00bfbe04)

~~~json
{
  "source": "00bfbe04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe08`](#insn-00bfbe08)

~~~json
{
  "source": "00bfbe08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe14`](#insn-00bfbe14)

~~~json
{
  "source": "00bfbe14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbe18`](#insn-00bfbe18)

~~~json
{
  "source": "00bfbe18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
