# 00b6faec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6fa24`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fa24.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0009.md#compare-a85b073b208fb5da4d08c91c07276399)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6fb30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fb30.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0010.md#compare-f23442cdd5eeae6d048495afb80db147)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6faec",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo5emailEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac408742e90b0cccec0dfa62a9cb2a369b7edddfb29b172acf8b08c8007590a2",
  "source_text_sha256": "ac408742e90b0cccec0dfa62a9cb2a369b7edddfb29b172acf8b08c8007590a2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6faec",
        "00b6fb6f"
      ]
    ],
    "bytes_sha256": "406d09811a4b31819816b6b2dcad13a15525da276a1b01a490585ce874f30623",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00bde090](../00bde/00bde090.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00bde4c0](../00bde/00bde4c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 644 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo5emailEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_0047495c(uVar2,lVar1,DAT_010a1aa0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6faec"></a> `00b6faec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b6faf0"></a> `00b6faf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6faf4"></a> `00b6faf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6faf8"></a> `00b6faf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b6fafc"></a> `00b6fafc` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00b6fb00"></a> `00b6fb00` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b6fb04"></a> `00b6fb04` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00b6fb08"></a> `00b6fb08` | `aa b9 01 94` | bl 0x00bde1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fb0c"></a> `00b6fb0c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6fb10"></a> `00b6fb10` | `f5 00 00 b4` | cbz x21,0x00b6fb2c | `CONDITIONAL_JUMP`
<a id="insn-00b6fb14"></a> `00b6fb14` | `88 29 00 d0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6fb18"></a> `00b6fb18` | `02 51 45 f9` | ldr x2,[x8, #0xaa0] | `FALL_THROUGH`
<a id="insn-00b6fb1c"></a> `00b6fb1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fb20"></a> `00b6fb20` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fb24"></a> `00b6fb24` | `8e 13 e4 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00b6fb28"></a> `00b6fb28` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b6fb2c"></a> `00b6fb2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fb30"></a> `00b6fb30` | `58 b9 01 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b6fb34"></a> `00b6fb34` | `35 01 00 b4` | cbz x21,0x00b6fb58 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb38"></a> `00b6fb38` | `00 01 00 37` | tbnz w0,#0x0,0x00b6fb58 | `CONDITIONAL_JUMP`
<a id="insn-00b6fb3c"></a> `00b6fb3c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b6fb40"></a> `00b6fb40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6fb44"></a> `00b6fb44` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fb48"></a> `00b6fb48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fb4c"></a> `00b6fb4c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b6fb50"></a> `00b6fb50` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fb54"></a> `00b6fb54` | `5b ba 01 14` | b 0x00bde4c0 | `CALL_TERMINATOR`
<a id="insn-00b6fb58"></a> `00b6fb58` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00b6fb5c"></a> `00b6fb5c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fb60"></a> `00b6fb60` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6fb64"></a> `00b6fb64` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6fb68"></a> `00b6fb68` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b6fb6c"></a> `00b6fb6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6faec`](#insn-00b6faec) 範囲 `[['00b6faec', '00b6fb13']]`
  - `CONDITIONAL_JUMP` [`00b6fb10`](#insn-00b6fb10) → [`00b6fb2c`](#insn-00b6fb2c)
  - `FALL_THROUGH` [`00b6fb10`](#insn-00b6fb10) → [`00b6fb14`](#insn-00b6fb14)
- ブロック [`00b6fb14`](#insn-00b6fb14) 範囲 `[['00b6fb14', '00b6fb2b']]`
  - `FALL_THROUGH` [`00b6fb28`](#insn-00b6fb28) → [`00b6fb2c`](#insn-00b6fb2c)
- ブロック [`00b6fb2c`](#insn-00b6fb2c) 範囲 `[['00b6fb2c', '00b6fb37']]`
  - `CONDITIONAL_JUMP` [`00b6fb34`](#insn-00b6fb34) → [`00b6fb58`](#insn-00b6fb58)
  - `FALL_THROUGH` [`00b6fb34`](#insn-00b6fb34) → [`00b6fb38`](#insn-00b6fb38)
- ブロック [`00b6fb38`](#insn-00b6fb38) 範囲 `[['00b6fb38', '00b6fb3b']]`
  - `CONDITIONAL_JUMP` [`00b6fb38`](#insn-00b6fb38) → [`00b6fb58`](#insn-00b6fb58)
  - `FALL_THROUGH` [`00b6fb38`](#insn-00b6fb38) → [`00b6fb3c`](#insn-00b6fb3c)
- ブロック [`00b6fb3c`](#insn-00b6fb3c) 範囲 `[['00b6fb3c', '00b6fb57']]`
- ブロック [`00b6fb58`](#insn-00b6fb58) 範囲 `[['00b6fb58', '00b6fb6f']]`

## 命令位置別の参照

- [`00b6faec`](#insn-00b6faec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6faf0`](#insn-00b6faf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6faf4`](#insn-00b6faf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb08`](#insn-00b6fb08) → [`00bde1b0`](../00bde/00bde1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb10`](#insn-00b6fb10) → [`00b6fb2c`](#insn-00b6fb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb18`](#insn-00b6fb18) → `010a1aa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6fb24`](#insn-00b6fb24) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb30`](#insn-00b6fb30) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb34`](#insn-00b6fb34) → [`00b6fb58`](#insn-00b6fb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb38`](#insn-00b6fb38) → [`00b6fb58`](#insn-00b6fb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb44`](#insn-00b6fb44) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb48`](#insn-00b6fb48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb54`](#insn-00b6fb54) → [`00bde4c0`](../00bde/00bde4c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde4c0` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb60`](#insn-00b6fb60) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6fb64`](#insn-00b6fb64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6faec`](#insn-00b6faec)

~~~json
{
  "source": "00b6faec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6faf0`](#insn-00b6faf0)

~~~json
{
  "source": "00b6faf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6faf4`](#insn-00b6faf4)

~~~json
{
  "source": "00b6faf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb08`](#insn-00b6fb08)

~~~json
{
  "source": "00b6fb08",
  "target": "00bde1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb10`](#insn-00b6fb10)

~~~json
{
  "source": "00b6fb10",
  "target": "00b6fb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb18`](#insn-00b6fb18)

~~~json
{
  "source": "00b6fb18",
  "target": "010a1aa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1aa0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6fb24`](#insn-00b6fb24)

~~~json
{
  "source": "00b6fb24",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb30`](#insn-00b6fb30)

~~~json
{
  "source": "00b6fb30",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb34`](#insn-00b6fb34)

~~~json
{
  "source": "00b6fb34",
  "target": "00b6fb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb38`](#insn-00b6fb38)

~~~json
{
  "source": "00b6fb38",
  "target": "00b6fb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb44`](#insn-00b6fb44)

~~~json
{
  "source": "00b6fb44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb48`](#insn-00b6fb48)

~~~json
{
  "source": "00b6fb48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb54`](#insn-00b6fb54)

~~~json
{
  "source": "00b6fb54",
  "target": "00bde4c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6fb60`](#insn-00b6fb60)

~~~json
{
  "source": "00b6fb60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6fb64`](#insn-00b6fb64)

~~~json
{
  "source": "00b6fb64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
