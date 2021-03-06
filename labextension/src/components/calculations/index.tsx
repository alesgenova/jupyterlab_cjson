import * as React from 'react';
import { Provider } from 'react-redux';
import {
  JSONObject
} from '@phosphor/coreutils';
import {MuiThemeProvider} from "material-ui/styles";

import './index.css';
import {store} from '../common'
import { CalculationMonitorTableContainer, authenticate } from 'mongochemclient'



export interface IProps {
  data: JSONObject;
  metadata?: JSONObject;
}

export default class CalculationMonitorComponent extends React.Component<IProps> {
  render() {
    const data = this.props.data;

    // Update the girder token from the notebook
    if ('girderToken' in data) {
      const girderToken = data['girderToken'];
      store.dispatch(authenticate(girderToken, false));
    }

    return (
     <div>
        <MuiThemeProvider>
          <Provider store={store}>
          <div>
            <CalculationMonitorTableContainer taskFlowIds={data.taskFlowIds} completeTitle={'Calculation(s) are complete. Please re-execute cell to view results.'} />
          </div>
          </Provider>
        </MuiThemeProvider>
      </div>
    );
  }
}
