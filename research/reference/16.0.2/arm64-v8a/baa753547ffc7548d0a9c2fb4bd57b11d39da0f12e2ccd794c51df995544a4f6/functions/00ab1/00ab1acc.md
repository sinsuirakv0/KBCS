# 00ab1acc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00ab1a5c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab1/00ab1a5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-36d2b13a349e60a5a78a33cc65576b69)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00ab2ac0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00ab2/00ab2ac0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-7dc129915bd94b3418b77dcdd424eb4a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ab1acc",
  "name": "FUN_00ab1acc",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c281f86d7d49f813689b6156dc4958a8c00536d4de98d6bb4a50ceac3fedb4f1",
  "source_text_sha256": "c281f86d7d49f813689b6156dc4958a8c00536d4de98d6bb4a50ceac3fedb4f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ab1acc",
        "00ab1b93"
      ]
    ],
    "bytes_sha256": "7fb9310d7502b7dd3389ef77cbd76f679ff5268d7f228493243834f7ee1746d3",
    "instruction_count": 50,
    "instruction_bytes": 200,
    "body_bytes": 200,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ab1808](../00ab1/00ab1808.md)

## 呼び出し先

- [00ab17a8](../00ab1/00ab17a8.md)
- [00ab17f4](../00ab1/00ab17f4.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c580d0](../00c58/00c580d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1251 bytes

~~~c

void FUN_00ab1acc(long *param_1,long param_2,undefined4 *param_3)

{
  long lVar1;
  undefined4 uVar2;
  size_t __n;
  long lVar3;
  void *__dest;
  undefined8 uVar4;
  void *pvVar5;
  undefined8 *puVar6;
  
  lVar3 = _Znwm(0x40);
  uVar2 = *param_3;
  *param_1 = lVar3;
  param_1[1] = param_2 + 8;
  *(undefined1 *)(param_1 + 2) = 0;
  *(undefined4 *)(lVar3 + 0x20) = uVar2;
  pvVar5 = *(void **)(param_3 + 2);
  lVar1 = *(long *)(param_3 + 4);
  puVar6 = (undefined8 *)(lVar3 + 0x28);
  *puVar6 = 0;
  *(undefined8 *)(lVar3 + 0x30) = 0;
  *(undefined8 *)(lVar3 + 0x38) = 0;
  __n = lVar1 - (long)pvVar5;
  if (__n != 0) {
    if ((long)__n < 0) {
      uVar4 = FUN_00ab17f4(puVar6);
      pvVar5 = (void *)*puVar6;
      if (pvVar5 != (void *)0x0) {
        *(void **)(lVar3 + 0x30) = pvVar5;
        _ZdlPv(pvVar5);
      }
      FUN_00ab17a8(param_1);
                    /* WARNING: Subroutine does not return */
      FUN_00c53ffc(uVar4);
    }
    __dest = (void *)_Znwm(__n);
    *(void **)(lVar3 + 0x28) = __dest;
    *(void **)(lVar3 + 0x30) = __dest;
    *(size_t *)(lVar3 + 0x38) = (long)__dest + __n;
    memcpy(__dest,pvVar5,__n);
    *(size_t *)(lVar3 + 0x30) = (long)__dest + __n;
  }
  *(undefined1 *)(param_1 + 2) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ab1acc"></a> `00ab1acc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00ab1ad0"></a> `00ab1ad0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab1ad4"></a> `00ab1ad4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1ad8"></a> `00ab1ad8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1adc"></a> `00ab1adc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ab1ae0"></a> `00ab1ae0` | `15 20 00 91` | add x21,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00ab1ae4"></a> `00ab1ae4` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab1ae8"></a> `00ab1ae8` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00ab1aec"></a> `00ab1aec` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00ab1af0"></a> `00ab1af0` | `1c 99 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1af4"></a> `00ab1af4` | `e8 02 40 b9` | ldr w8,[x23] | `FALL_THROUGH`
<a id="insn-00ab1af8"></a> `00ab1af8` | `60 56 00 a9` | stp x0,x21,[x19] | `FALL_THROUGH`
<a id="insn-00ab1afc"></a> `00ab1afc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab1b00"></a> `00ab1b00` | `7f 42 00 39` | strb wzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ab1b04"></a> `00ab1b04` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1b08"></a> `00ab1b08` | `f6 a2 40 a9` | ldp x22,x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00ab1b0c"></a> `00ab1b0c` | `bf 8e 02 f8` | str xzr,[x21, #0x28]! | `FALL_THROUGH`
<a id="insn-00ab1b10"></a> `00ab1b10` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1b14"></a> `00ab1b14` | `17 01 16 eb` | subs x23,x8,x22 | `FALL_THROUGH`
<a id="insn-00ab1b18"></a> `00ab1b18` | `80 01 00 54` | b.eq 0x00ab1b48 | `CONDITIONAL_JUMP`
<a id="insn-00ab1b1c"></a> `00ab1b1c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ab1b20"></a> `00ab1b20` | `37 02 f8 b7` | tbnz x23,#0x3f,0x00ab1b64 | `CONDITIONAL_JUMP`
<a id="insn-00ab1b24"></a> `00ab1b24` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ab1b28"></a> `00ab1b28` | `0e 99 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1b2c"></a> `00ab1b2c` | `15 00 17 8b` | add x21,x0,x23 | `FALL_THROUGH`
<a id="insn-00ab1b30"></a> `00ab1b30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00ab1b34"></a> `00ab1b34` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00ab1b38"></a> `00ab1b38` | `80 82 02 a9` | stp x0,x0,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab1b3c"></a> `00ab1b3c` | `95 1e 00 f9` | str x21,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab1b40"></a> `00ab1b40` | `64 99 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1b44"></a> `00ab1b44` | `95 1a 00 f9` | str x21,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1b48"></a> `00ab1b48` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1b4c"></a> `00ab1b4c` | `68 42 00 39` | strb w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ab1b50"></a> `00ab1b50` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1b54"></a> `00ab1b54` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab1b58"></a> `00ab1b58` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1b5c"></a> `00ab1b5c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00ab1b60"></a> `00ab1b60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ab1b64"></a> `00ab1b64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ab1b68"></a> `00ab1b68` | `23 ff ff 97` | bl 0x00ab17f4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1b6c"></a> `00ab1b6c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ab1b70"></a> `00ab1b70` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab1b74"></a> `00ab1b74` | `88 00 00 b4` | cbz x8,0x00ab1b84 | `CONDITIONAL_JUMP`
<a id="insn-00ab1b78"></a> `00ab1b78` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00ab1b7c"></a> `00ab1b7c` | `88 1a 00 f9` | str x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1b80"></a> `00ab1b80` | `00 99 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1b84"></a> `00ab1b84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ab1b88"></a> `00ab1b88` | `08 ff ff 97` | bl 0x00ab17a8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1b8c"></a> `00ab1b8c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ab1b90"></a> `00ab1b90` | `1b 89 06 94` | bl 0x00c53ffc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ab1acc`](#insn-00ab1acc) 範囲 `[['00ab1acc', '00ab1b1b']]`
  - `CONDITIONAL_JUMP` [`00ab1b18`](#insn-00ab1b18) → [`00ab1b48`](#insn-00ab1b48)
  - `FALL_THROUGH` [`00ab1b18`](#insn-00ab1b18) → [`00ab1b1c`](#insn-00ab1b1c)
- ブロック [`00ab1b1c`](#insn-00ab1b1c) 範囲 `[['00ab1b1c', '00ab1b23']]`
  - `CONDITIONAL_JUMP` [`00ab1b20`](#insn-00ab1b20) → [`00ab1b64`](#insn-00ab1b64)
  - `FALL_THROUGH` [`00ab1b20`](#insn-00ab1b20) → [`00ab1b24`](#insn-00ab1b24)
- ブロック [`00ab1b24`](#insn-00ab1b24) 範囲 `[['00ab1b24', '00ab1b47']]`
  - `FALL_THROUGH` [`00ab1b44`](#insn-00ab1b44) → [`00ab1b48`](#insn-00ab1b48)
- ブロック [`00ab1b48`](#insn-00ab1b48) 範囲 `[['00ab1b48', '00ab1b63']]`
- ブロック [`00ab1b64`](#insn-00ab1b64) 範囲 `[['00ab1b64', '00ab1b77']]`
  - `CONDITIONAL_JUMP` [`00ab1b74`](#insn-00ab1b74) → [`00ab1b84`](#insn-00ab1b84)
  - `FALL_THROUGH` [`00ab1b74`](#insn-00ab1b74) → [`00ab1b78`](#insn-00ab1b78)
- ブロック [`00ab1b78`](#insn-00ab1b78) 範囲 `[['00ab1b78', '00ab1b83']]`
  - `FALL_THROUGH` [`00ab1b80`](#insn-00ab1b80) → [`00ab1b84`](#insn-00ab1b84)
- ブロック [`00ab1b84`](#insn-00ab1b84) 範囲 `[['00ab1b84', '00ab1b93']]`

## 命令位置別の参照

- [`00ab1acc`](#insn-00ab1acc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ad0`](#insn-00ab1ad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ad4`](#insn-00ab1ad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1ad8`](#insn-00ab1ad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1af0`](#insn-00ab1af0) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b18`](#insn-00ab1b18) → [`00ab1b48`](#insn-00ab1b48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b20`](#insn-00ab1b20) → [`00ab1b64`](#insn-00ab1b64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b28`](#insn-00ab1b28) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b40`](#insn-00ab1b40) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b50`](#insn-00ab1b50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b54`](#insn-00ab1b54) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b58`](#insn-00ab1b58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b5c`](#insn-00ab1b5c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b68`](#insn-00ab1b68) → [`00ab17f4`](00ab17f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab17f4` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b74`](#insn-00ab1b74) → [`00ab1b84`](#insn-00ab1b84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b80`](#insn-00ab1b80) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b88`](#insn-00ab1b88) → [`00ab17a8`](00ab17a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab17a8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1b90`](#insn-00ab1b90) → [`00c53ffc`](../00c53/00c53ffc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53ffc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ab1acc`](#insn-00ab1acc)

~~~json
{
  "source": "00ab1acc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1ad0`](#insn-00ab1ad0)

~~~json
{
  "source": "00ab1ad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1ad4`](#insn-00ab1ad4)

~~~json
{
  "source": "00ab1ad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1ad8`](#insn-00ab1ad8)

~~~json
{
  "source": "00ab1ad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1af0`](#insn-00ab1af0)

~~~json
{
  "source": "00ab1af0",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1b18`](#insn-00ab1b18)

~~~json
{
  "source": "00ab1b18",
  "target": "00ab1b48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b20`](#insn-00ab1b20)

~~~json
{
  "source": "00ab1b20",
  "target": "00ab1b64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b28`](#insn-00ab1b28)

~~~json
{
  "source": "00ab1b28",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1b40`](#insn-00ab1b40)

~~~json
{
  "source": "00ab1b40",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1b50`](#insn-00ab1b50)

~~~json
{
  "source": "00ab1b50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b54`](#insn-00ab1b54)

~~~json
{
  "source": "00ab1b54",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b58`](#insn-00ab1b58)

~~~json
{
  "source": "00ab1b58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b5c`](#insn-00ab1b5c)

~~~json
{
  "source": "00ab1b5c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b68`](#insn-00ab1b68)

~~~json
{
  "source": "00ab1b68",
  "target": "00ab17f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1b74`](#insn-00ab1b74)

~~~json
{
  "source": "00ab1b74",
  "target": "00ab1b84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1b80`](#insn-00ab1b80)

~~~json
{
  "source": "00ab1b80",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1b88`](#insn-00ab1b88)

~~~json
{
  "source": "00ab1b88",
  "target": "00ab17a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1b90`](#insn-00ab1b90)

~~~json
{
  "source": "00ab1b90",
  "target": "00c53ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
