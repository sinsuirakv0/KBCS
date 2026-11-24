# 00b2aaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b2aa10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aa10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0037.md#compare-f0b4b7bc6318714843adb94cb4b4d223)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b2baa0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2b/00b2baa0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0030.md#compare-8e635dc52b3c69c0833f4bdc3e5770f6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2aaac",
  "name": "FUN_00b2aaac",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "901602ab7ad2721004c5a8d14a1dbd745ed9e8115c746ff441e6601a4a4b95a1",
  "source_text_sha256": "901602ab7ad2721004c5a8d14a1dbd745ed9e8115c746ff441e6601a4a4b95a1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2aaac",
        "00b2ab4b"
      ]
    ],
    "bytes_sha256": "0990dc1960ecc09f0d70666b64378a1489e0a22db823df536c28563270131703",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 858 bytes

~~~c

void FUN_00b2aaac(undefined8 *param_1)

{
  long lVar1;
  void *__ptr;
  long lVar2;
  
  lVar1 = param_1[1];
  lVar2 = param_1[2];
  do {
    if (lVar2 == lVar1) {
      if ((void *)*param_1 != (void *)0x0) {
        _ZdlPv((void *)*param_1);
        return;
      }
      return;
    }
    param_1[2] = lVar2 + -0x60;
    if ((*(byte *)(lVar2 + -0x18) & 1) == 0) {
      if ((*(byte *)(lVar2 + -0x30) & 1) == 0) goto LAB_00b2aaec;
LAB_00b2ab08:
      _ZdlPv(*(void **)(lVar2 + -0x20));
      __ptr = *(void **)(lVar2 + -0x48);
    }
    else {
      _ZdlPv(*(void **)(lVar2 + -8));
      if ((*(byte *)(lVar2 + -0x30) & 1) != 0) goto LAB_00b2ab08;
LAB_00b2aaec:
      __ptr = *(void **)(lVar2 + -0x48);
    }
    if (__ptr != (void *)0x0) {
      *(void **)(lVar2 + -0x40) = __ptr;
      _ZdlPv(__ptr);
    }
    lVar2 = param_1[2];
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2aaac"></a> `00b2aaac` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b2aab0"></a> `00b2aab0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aab4"></a> `00b2aab4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2aab8"></a> `00b2aab8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b2aabc"></a> `00b2aabc` | `14 d4 40 a9` | ldp x20,x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00b2aac0"></a> `00b2aac0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b2aac4"></a> `00b2aac4` | `02 00 00 14` | b 0x00b2aacc | `UNCONDITIONAL_JUMP`
<a id="insn-00b2aac8"></a> `00b2aac8` | `75 0a 40 f9` | ldr x21,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aacc"></a> `00b2aacc` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00b2aad0"></a> `00b2aad0` | `a0 02 00 54` | b.eq 0x00b2ab24 | `CONDITIONAL_JUMP`
<a id="insn-00b2aad4"></a> `00b2aad4` | `a8 82 01 d1` | sub x8,x21,#0x60 | `FALL_THROUGH`
<a id="insn-00b2aad8"></a> `00b2aad8` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2aadc"></a> `00b2aadc` | `a8 82 5e 38` | ldurb w8,[x21, #-0x18] | `FALL_THROUGH`
<a id="insn-00b2aae0"></a> `00b2aae0` | `c8 00 00 37` | tbnz w8,#0x0,0x00b2aaf8 | `CONDITIONAL_JUMP`
<a id="insn-00b2aae4"></a> `00b2aae4` | `a8 02 5d 38` | ldurb w8,[x21, #-0x30] | `FALL_THROUGH`
<a id="insn-00b2aae8"></a> `00b2aae8` | `08 01 00 37` | tbnz w8,#0x0,0x00b2ab08 | `CONDITIONAL_JUMP`
<a id="insn-00b2aaec"></a> `00b2aaec` | `a0 82 5b f8` | ldur x0,[x21, #-0x48] | `FALL_THROUGH`
<a id="insn-00b2aaf0"></a> `00b2aaf0` | `40 01 00 b5` | cbnz x0,0x00b2ab18 | `CONDITIONAL_JUMP`
<a id="insn-00b2aaf4"></a> `00b2aaf4` | `f5 ff ff 17` | b 0x00b2aac8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2aaf8"></a> `00b2aaf8` | `a0 82 5f f8` | ldur x0,[x21, #-0x8] | `FALL_THROUGH`
<a id="insn-00b2aafc"></a> `00b2aafc` | `21 b5 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ab00"></a> `00b2ab00` | `a8 02 5d 38` | ldurb w8,[x21, #-0x30] | `FALL_THROUGH`
<a id="insn-00b2ab04"></a> `00b2ab04` | `48 ff 07 36` | tbz w8,#0x0,0x00b2aaec | `CONDITIONAL_JUMP`
<a id="insn-00b2ab08"></a> `00b2ab08` | `a0 02 5e f8` | ldur x0,[x21, #-0x20] | `FALL_THROUGH`
<a id="insn-00b2ab0c"></a> `00b2ab0c` | `1d b5 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ab10"></a> `00b2ab10` | `a0 82 5b f8` | ldur x0,[x21, #-0x48] | `FALL_THROUGH`
<a id="insn-00b2ab14"></a> `00b2ab14` | `a0 fd ff b4` | cbz x0,0x00b2aac8 | `CONDITIONAL_JUMP`
<a id="insn-00b2ab18"></a> `00b2ab18` | `a0 02 1c f8` | stur x0,[x21, #-0x40] | `FALL_THROUGH`
<a id="insn-00b2ab1c"></a> `00b2ab1c` | `19 b5 04 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ab20"></a> `00b2ab20` | `ea ff ff 17` | b 0x00b2aac8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ab24"></a> `00b2ab24` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00b2ab28"></a> `00b2ab28` | `a0 00 00 b4` | cbz x0,0x00b2ab3c | `CONDITIONAL_JUMP`
<a id="insn-00b2ab2c"></a> `00b2ab2c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ab30"></a> `00b2ab30` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ab34"></a> `00b2ab34` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b2ab38"></a> `00b2ab38` | `12 b5 04 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00b2ab3c"></a> `00b2ab3c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ab40"></a> `00b2ab40` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ab44"></a> `00b2ab44` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b2ab48"></a> `00b2ab48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2aaac`](#insn-00b2aaac) 範囲 `[['00b2aaac', '00b2aac7']]`
  - `UNCONDITIONAL_JUMP` [`00b2aac4`](#insn-00b2aac4) → [`00b2aacc`](#insn-00b2aacc)
- ブロック [`00b2aac8`](#insn-00b2aac8) 範囲 `[['00b2aac8', '00b2aacb']]`
  - `FALL_THROUGH` [`00b2aac8`](#insn-00b2aac8) → [`00b2aacc`](#insn-00b2aacc)
- ブロック [`00b2aacc`](#insn-00b2aacc) 範囲 `[['00b2aacc', '00b2aad3']]`
  - `CONDITIONAL_JUMP` [`00b2aad0`](#insn-00b2aad0) → [`00b2ab24`](#insn-00b2ab24)
  - `FALL_THROUGH` [`00b2aad0`](#insn-00b2aad0) → [`00b2aad4`](#insn-00b2aad4)
- ブロック [`00b2aad4`](#insn-00b2aad4) 範囲 `[['00b2aad4', '00b2aae3']]`
  - `CONDITIONAL_JUMP` [`00b2aae0`](#insn-00b2aae0) → [`00b2aaf8`](#insn-00b2aaf8)
  - `FALL_THROUGH` [`00b2aae0`](#insn-00b2aae0) → [`00b2aae4`](#insn-00b2aae4)
- ブロック [`00b2aae4`](#insn-00b2aae4) 範囲 `[['00b2aae4', '00b2aaeb']]`
  - `CONDITIONAL_JUMP` [`00b2aae8`](#insn-00b2aae8) → [`00b2ab08`](#insn-00b2ab08)
  - `FALL_THROUGH` [`00b2aae8`](#insn-00b2aae8) → [`00b2aaec`](#insn-00b2aaec)
- ブロック [`00b2aaec`](#insn-00b2aaec) 範囲 `[['00b2aaec', '00b2aaf3']]`
  - `CONDITIONAL_JUMP` [`00b2aaf0`](#insn-00b2aaf0) → [`00b2ab18`](#insn-00b2ab18)
  - `FALL_THROUGH` [`00b2aaf0`](#insn-00b2aaf0) → [`00b2aaf4`](#insn-00b2aaf4)
- ブロック [`00b2aaf4`](#insn-00b2aaf4) 範囲 `[['00b2aaf4', '00b2aaf7']]`
  - `UNCONDITIONAL_JUMP` [`00b2aaf4`](#insn-00b2aaf4) → [`00b2aac8`](#insn-00b2aac8)
- ブロック [`00b2aaf8`](#insn-00b2aaf8) 範囲 `[['00b2aaf8', '00b2ab07']]`
  - `CONDITIONAL_JUMP` [`00b2ab04`](#insn-00b2ab04) → [`00b2aaec`](#insn-00b2aaec)
  - `FALL_THROUGH` [`00b2ab04`](#insn-00b2ab04) → [`00b2ab08`](#insn-00b2ab08)
- ブロック [`00b2ab08`](#insn-00b2ab08) 範囲 `[['00b2ab08', '00b2ab17']]`
  - `CONDITIONAL_JUMP` [`00b2ab14`](#insn-00b2ab14) → [`00b2aac8`](#insn-00b2aac8)
  - `FALL_THROUGH` [`00b2ab14`](#insn-00b2ab14) → [`00b2ab18`](#insn-00b2ab18)
- ブロック [`00b2ab18`](#insn-00b2ab18) 範囲 `[['00b2ab18', '00b2ab23']]`
  - `UNCONDITIONAL_JUMP` [`00b2ab20`](#insn-00b2ab20) → [`00b2aac8`](#insn-00b2aac8)
- ブロック [`00b2ab24`](#insn-00b2ab24) 範囲 `[['00b2ab24', '00b2ab2b']]`
  - `CONDITIONAL_JUMP` [`00b2ab28`](#insn-00b2ab28) → [`00b2ab3c`](#insn-00b2ab3c)
  - `FALL_THROUGH` [`00b2ab28`](#insn-00b2ab28) → [`00b2ab2c`](#insn-00b2ab2c)
- ブロック [`00b2ab2c`](#insn-00b2ab2c) 範囲 `[['00b2ab2c', '00b2ab3b']]`
- ブロック [`00b2ab3c`](#insn-00b2ab3c) 範囲 `[['00b2ab3c', '00b2ab4b']]`

## 命令位置別の参照

- [`00b2aaac`](#insn-00b2aaac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aab0`](#insn-00b2aab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aab4`](#insn-00b2aab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aac4`](#insn-00b2aac4) → [`00b2aacc`](#insn-00b2aacc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aad0`](#insn-00b2aad0) → [`00b2ab24`](#insn-00b2ab24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aae0`](#insn-00b2aae0) → [`00b2aaf8`](#insn-00b2aaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aae8`](#insn-00b2aae8) → [`00b2ab08`](#insn-00b2ab08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aaf0`](#insn-00b2aaf0) → [`00b2ab18`](#insn-00b2ab18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aaf4`](#insn-00b2aaf4) → [`00b2aac8`](#insn-00b2aac8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2aafc`](#insn-00b2aafc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab04`](#insn-00b2ab04) → [`00b2aaec`](#insn-00b2aaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab0c`](#insn-00b2ab0c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab14`](#insn-00b2ab14) → [`00b2aac8`](#insn-00b2aac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab1c`](#insn-00b2ab1c) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab20`](#insn-00b2ab20) → [`00b2aac8`](#insn-00b2aac8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab28`](#insn-00b2ab28) → [`00b2ab3c`](#insn-00b2ab3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab2c`](#insn-00b2ab2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab30`](#insn-00b2ab30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab34`](#insn-00b2ab34) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab38`](#insn-00b2ab38) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab3c`](#insn-00b2ab3c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab40`](#insn-00b2ab40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ab44`](#insn-00b2ab44) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2aaac`](#insn-00b2aaac)

~~~json
{
  "source": "00b2aaac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aab0`](#insn-00b2aab0)

~~~json
{
  "source": "00b2aab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aab4`](#insn-00b2aab4)

~~~json
{
  "source": "00b2aab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aac4`](#insn-00b2aac4)

~~~json
{
  "source": "00b2aac4",
  "target": "00b2aacc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aad0`](#insn-00b2aad0)

~~~json
{
  "source": "00b2aad0",
  "target": "00b2ab24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aae0`](#insn-00b2aae0)

~~~json
{
  "source": "00b2aae0",
  "target": "00b2aaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aae8`](#insn-00b2aae8)

~~~json
{
  "source": "00b2aae8",
  "target": "00b2ab08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aaf0`](#insn-00b2aaf0)

~~~json
{
  "source": "00b2aaf0",
  "target": "00b2ab18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aaf4`](#insn-00b2aaf4)

~~~json
{
  "source": "00b2aaf4",
  "target": "00b2aac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2aafc`](#insn-00b2aafc)

~~~json
{
  "source": "00b2aafc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ab04`](#insn-00b2ab04)

~~~json
{
  "source": "00b2ab04",
  "target": "00b2aaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab0c`](#insn-00b2ab0c)

~~~json
{
  "source": "00b2ab0c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ab14`](#insn-00b2ab14)

~~~json
{
  "source": "00b2ab14",
  "target": "00b2aac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab1c`](#insn-00b2ab1c)

~~~json
{
  "source": "00b2ab1c",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ab20`](#insn-00b2ab20)

~~~json
{
  "source": "00b2ab20",
  "target": "00b2aac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab28`](#insn-00b2ab28)

~~~json
{
  "source": "00b2ab28",
  "target": "00b2ab3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab2c`](#insn-00b2ab2c)

~~~json
{
  "source": "00b2ab2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab30`](#insn-00b2ab30)

~~~json
{
  "source": "00b2ab30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab34`](#insn-00b2ab34)

~~~json
{
  "source": "00b2ab34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab38`](#insn-00b2ab38)

~~~json
{
  "source": "00b2ab38",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ab3c`](#insn-00b2ab3c)

~~~json
{
  "source": "00b2ab3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab40`](#insn-00b2ab40)

~~~json
{
  "source": "00b2ab40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ab44`](#insn-00b2ab44)

~~~json
{
  "source": "00b2ab44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
