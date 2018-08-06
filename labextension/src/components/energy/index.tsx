import * as React from 'react';
import {
  JSONObject
} from '@phosphor/coreutils';

import { wc } from '../common/webcomponent';

export interface IProps {
  data: JSONObject;
  metadata?: JSONObject;
}

export default class FreeEnergyComponent extends React.Component<IProps> {

  render() {
    const data: any = this.props.data;
    if (!data.freeEnergy || !data.reaction || data.freeEnergy.length != data.reaction.length) {
      return null;
    }

    let energies = [];
    for (let i = 0; i < data.freeEnergy.length; ++i) {
      energies.push({
        energy: data.freeEnergy[i],
        label: data.reaction[i]
      })
    }

    let energyPlot: any = <oc-energy-plot />
    energyPlot.ref = wc(
      // Events
      {},
      // Props
      {
        energies
      }
    );

    return (
      <div style={{width: '100%', height: '40rem'}}>
        {energyPlot}
      </div>
    );
  }
}
