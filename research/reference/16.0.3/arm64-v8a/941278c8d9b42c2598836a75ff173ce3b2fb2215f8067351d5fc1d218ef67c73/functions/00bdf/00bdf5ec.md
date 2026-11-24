# 00bdf5ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bde5f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde5f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-3dd8c10c6b86bfbc87c0561beb221af9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf5ec",
  "name": "_ZNK8firebase4auth4User9photo_urlEv",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fd9dbebbaab874f8c7faf0f69adf00b62f70c256dc652a54492d4d759c25b12",
  "source_text_sha256": "6fd9dbebbaab874f8c7faf0f69adf00b62f70c256dc652a54492d4d759c25b12",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf5ec",
        "00bdf68f"
      ]
    ],
    "bytes_sha256": "e5c70be93b3b3a11f293b9f90bcffad580d2cd7248332ba6b49e4f119da2499b",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c390](../00c5c/00c5c390.md)
- [00c5c660](../00c5c/00c5c660.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 790 bytes

~~~c

void _ZNK8firebase4auth4User9photo_urlEv(undefined8 *param_1,long param_2)

{
  undefined8 uVar1;
  ulong uVar2;
  undefined8 *puVar3;
  long lVar4;
  
  puVar3 = *(undefined8 **)(param_2 + 0x98);
  if ((puVar3 == (undefined8 *)0x0) || (lVar4 = puVar3[0x40], lVar4 == 0)) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
              (param_1,&DAT_002a64e6);
    return;
  }
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*puVar3);
  lVar4 = FUN_00497b94(uVar1,lVar4,DAT_01127ea0);
  uVar2 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  if ((lVar4 != 0) && ((uVar2 & 1) == 0)) {
    _ZN8firebase4util14JniUriToStringEP7_JNIEnvP8_jobject(param_1,uVar1,lVar4);
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
<a id="insn-00bdf5ec"></a> `00bdf5ec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdf5f0"></a> `00bdf5f0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf5f4"></a> `00bdf5f4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf5f8"></a> `00bdf5f8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdf5fc"></a> `00bdf5fc` | `09 4c 40 f9` | ldr x9,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf600"></a> `00bdf600` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdf604"></a> `00bdf604` | `c9 02 00 b4` | cbz x9,0x00bdf65c | `CONDITIONAL_JUMP`
<a id="insn-00bdf608"></a> `00bdf608` | `35 01 41 f9` | ldr x21,[x9, #0x200] | `FALL_THROUGH`
<a id="insn-00bdf60c"></a> `00bdf60c` | `95 02 00 b4` | cbz x21,0x00bdf65c | `CONDITIONAL_JUMP`
<a id="insn-00bdf610"></a> `00bdf610` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdf614"></a> `00bdf614` | `c3 f2 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf618"></a> `00bdf618` | `48 2a 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdf61c"></a> `00bdf61c` | `02 51 47 f9` | ldr x2,[x8, #0xea0] | `FALL_THROUGH`
<a id="insn-00bdf620"></a> `00bdf620` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf624"></a> `00bdf624` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdf628"></a> `00bdf628` | `5b e1 e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf62c"></a> `00bdf62c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdf630"></a> `00bdf630` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf634"></a> `00bdf634` | `73 f2 01 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf638"></a> `00bdf638` | `15 02 00 b4` | cbz x21,0x00bdf678 | `CONDITIONAL_JUMP`
<a id="insn-00bdf63c"></a> `00bdf63c` | `e0 01 00 37` | tbnz w0,#0x0,0x00bdf678 | `CONDITIONAL_JUMP`
<a id="insn-00bdf640"></a> `00bdf640` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bdf644"></a> `00bdf644` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf648"></a> `00bdf648` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf64c"></a> `00bdf64c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf650"></a> `00bdf650` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf654"></a> `00bdf654` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf658"></a> `00bdf658` | `4e f3 01 14` | b 0x00c5c390 | `CALL_TERMINATOR`
<a id="insn-00bdf65c"></a> `00bdf65c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdf660"></a> `00bdf660` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf664"></a> `00bdf664` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf668"></a> `00bdf668` | `21 b6 ff f0` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bdf66c"></a> `00bdf66c` | `21 98 13 91` | add x1,x1,#0x4e6 | `FALL_THROUGH`
<a id="insn-00bdf670"></a> `00bdf670` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf674"></a> `00bdf674` | `fb f3 01 14` | b 0x00c5c660 | `CALL_TERMINATOR`
<a id="insn-00bdf678"></a> `00bdf678` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdf67c"></a> `00bdf67c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf680"></a> `00bdf680` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf684"></a> `00bdf684` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf688"></a> `00bdf688` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf68c"></a> `00bdf68c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf5ec`](#insn-00bdf5ec) 範囲 `[['00bdf5ec', '00bdf607']]`
  - `CONDITIONAL_JUMP` [`00bdf604`](#insn-00bdf604) → [`00bdf65c`](#insn-00bdf65c)
  - `FALL_THROUGH` [`00bdf604`](#insn-00bdf604) → [`00bdf608`](#insn-00bdf608)
- ブロック [`00bdf608`](#insn-00bdf608) 範囲 `[['00bdf608', '00bdf60f']]`
  - `CONDITIONAL_JUMP` [`00bdf60c`](#insn-00bdf60c) → [`00bdf65c`](#insn-00bdf65c)
  - `FALL_THROUGH` [`00bdf60c`](#insn-00bdf60c) → [`00bdf610`](#insn-00bdf610)
- ブロック [`00bdf610`](#insn-00bdf610) 範囲 `[['00bdf610', '00bdf63b']]`
  - `CONDITIONAL_JUMP` [`00bdf638`](#insn-00bdf638) → [`00bdf678`](#insn-00bdf678)
  - `FALL_THROUGH` [`00bdf638`](#insn-00bdf638) → [`00bdf63c`](#insn-00bdf63c)
- ブロック [`00bdf63c`](#insn-00bdf63c) 範囲 `[['00bdf63c', '00bdf63f']]`
  - `CONDITIONAL_JUMP` [`00bdf63c`](#insn-00bdf63c) → [`00bdf678`](#insn-00bdf678)
  - `FALL_THROUGH` [`00bdf63c`](#insn-00bdf63c) → [`00bdf640`](#insn-00bdf640)
- ブロック [`00bdf640`](#insn-00bdf640) 範囲 `[['00bdf640', '00bdf65b']]`
- ブロック [`00bdf65c`](#insn-00bdf65c) 範囲 `[['00bdf65c', '00bdf677']]`
- ブロック [`00bdf678`](#insn-00bdf678) 範囲 `[['00bdf678', '00bdf68f']]`

## 命令位置別の参照

- [`00bdf5ec`](#insn-00bdf5ec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf5f0`](#insn-00bdf5f0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf5f4`](#insn-00bdf5f4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf604`](#insn-00bdf604) → [`00bdf65c`](#insn-00bdf65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf60c`](#insn-00bdf60c) → [`00bdf65c`](#insn-00bdf65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf614`](#insn-00bdf614) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdf61c`](#insn-00bdf61c) → `01127ea0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf628`](#insn-00bdf628) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdf634`](#insn-00bdf634) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdf638`](#insn-00bdf638) → [`00bdf678`](#insn-00bdf678) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf63c`](#insn-00bdf63c) → [`00bdf678`](#insn-00bdf678) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf648`](#insn-00bdf648) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf64c`](#insn-00bdf64c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf658`](#insn-00bdf658) → [`00c5c390`](../00c5c/00c5c390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c390` · 推定シンボル `None` · 推定型 `None`
- [`00bdf660`](#insn-00bdf660) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf664`](#insn-00bdf664) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf66c`](#insn-00bdf66c) → `002a64e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdf674`](#insn-00bdf674) → [`00c5c660`](../00c5c/00c5c660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c660` · 推定シンボル `None` · 推定型 `None`
- [`00bdf680`](#insn-00bdf680) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf684`](#insn-00bdf684) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf5ec`](#insn-00bdf5ec)

~~~json
{
  "source": "00bdf5ec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf5f0`](#insn-00bdf5f0)

~~~json
{
  "source": "00bdf5f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf5f4`](#insn-00bdf5f4)

~~~json
{
  "source": "00bdf5f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf604`](#insn-00bdf604)

~~~json
{
  "source": "00bdf604",
  "target": "00bdf65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf60c`](#insn-00bdf60c)

~~~json
{
  "source": "00bdf60c",
  "target": "00bdf65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf614`](#insn-00bdf614)

~~~json
{
  "source": "00bdf614",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf61c`](#insn-00bdf61c)

~~~json
{
  "source": "00bdf61c",
  "target": "01127ea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf628`](#insn-00bdf628)

~~~json
{
  "source": "00bdf628",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf634`](#insn-00bdf634)

~~~json
{
  "source": "00bdf634",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf638`](#insn-00bdf638)

~~~json
{
  "source": "00bdf638",
  "target": "00bdf678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf63c`](#insn-00bdf63c)

~~~json
{
  "source": "00bdf63c",
  "target": "00bdf678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf648`](#insn-00bdf648)

~~~json
{
  "source": "00bdf648",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf64c`](#insn-00bdf64c)

~~~json
{
  "source": "00bdf64c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf658`](#insn-00bdf658)

~~~json
{
  "source": "00bdf658",
  "target": "00c5c390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf660`](#insn-00bdf660)

~~~json
{
  "source": "00bdf660",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf664`](#insn-00bdf664)

~~~json
{
  "source": "00bdf664",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf66c`](#insn-00bdf66c)

~~~json
{
  "source": "00bdf66c",
  "target": "002a64e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a64e6",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a64e6",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdf674`](#insn-00bdf674)

~~~json
{
  "source": "00bdf674",
  "target": "00c5c660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf680`](#insn-00bdf680)

~~~json
{
  "source": "00bdf680",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf684`](#insn-00bdf684)

~~~json
{
  "source": "00bdf684",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
